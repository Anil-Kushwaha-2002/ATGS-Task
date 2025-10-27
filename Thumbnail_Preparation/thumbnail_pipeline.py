# thumbnail_pipeline.py
import os
import io
import sys
from multiprocessing import Process, Queue, cpu_count
from PIL import Image
from pathlib import Path
import time

PRODUCER_DIR = Path("producer")
CONSUMER_DIR = Path("consumer")
THUMBNAIL_SIZE = (200, 200)  # change as needed

def create_thumbnail_bytes(image_path: Path, size=THUMBNAIL_SIZE):
    with Image.open(image_path) as img:
        img.thumbnail(size)
        buf = io.BytesIO()
        # convert to RGB to avoid saving issues with PNG transparency etc.
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.save(buf, format="JPEG")
        buf.seek(0)
        return buf.read()

def producer_task(q: Queue, producer_dir: Path, num_consumers: int):
    converted_count = 0
    for p in sorted(producer_dir.iterdir()):
        if p.is_file():
            try:
                thumb_bytes = create_thumbnail_bytes(p)
                # send tuple (filename_stem, bytes)
                q.put((p.stem, thumb_bytes))
                converted_count += 1
            except Exception as e:
                print(f"[Producer] Error processing {p}: {e}", file=sys.stderr)
    # send sentinel for each consumer
    for _ in range(num_consumers):
        q.put(None)
    print(f"[Producer] Produced thumbnails for {converted_count} files and sent sentinel(s).")

def consumer_task(q: Queue, consumer_dir: Path, consumer_id: int, result_q: Queue = None):
    saved = 0
    while True:
        item = q.get()
        if item is None:
            # put sentinel back for other consumers if you popped a shared sentinel? (not necessary here)
            break
        name_stem, thumb_bytes = item
        try:
            out_name = consumer_dir / f"{name_stem}-thumbnail.jpg"
            # write bytes to file
            with open(out_name, "wb") as f:
                f.write(thumb_bytes)
            saved += 1
        except Exception as e:
            print(f"[Consumer {consumer_id}] Error saving {name_stem}: {e}", file=sys.stderr)
    if result_q:
        result_q.put(saved)
    print(f"[Consumer {consumer_id}] Exiting. Saved {saved} images.")

def ensure_dirs():
    PRODUCER_DIR.mkdir(parents=True, exist_ok=True)
    CONSUMER_DIR.mkdir(parents=True, exist_ok=True)

def main(num_consumers: int = None):
    ensure_dirs()
    if num_consumers is None:
        num_consumers = max(1, cpu_count() - 1)
    q = Queue(maxsize= num_consumers * 2 + 10)
    result_q = Queue()

    producer = Process(target=producer_task, args=(q, PRODUCER_DIR, num_consumers), name="Producer")
    consumers = [
        Process(target=consumer_task, args=(q, CONSUMER_DIR, i, result_q), name=f"Consumer-{i}")
        for i in range(num_consumers)
    ]

    start = time.time()
    producer.start()
    for c in consumers:
        c.start()

    # wait for producer
    producer.join()
    # wait for consumers
    for c in consumers:
        c.join()

    total_saved = 0
    while not result_q.empty():
        total_saved += result_q.get()

    elapsed = time.time() - start
    print(f"\nMain: Total images saved by consumers: {total_saved}")
    print(f"Main: Time elapsed: {elapsed:.2f} sec")

if __name__ == "__main__":
    # optionally accept number of consumers as CLI arg
    arg = None
    if len(sys.argv) > 1:
        try:
            arg = int(sys.argv[1])
        except:
            arg = None
    main(num_consumers=arg)
