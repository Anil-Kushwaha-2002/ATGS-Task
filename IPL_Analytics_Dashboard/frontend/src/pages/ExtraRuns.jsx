import React, {useState} from 'react';
import axios from 'axios';
import ChartWrapper from '../components/ChartWrapper';
import { Container, TextField, Button } from '@mui/material';

export default function ExtraRuns(){
  const [year, setYear] = useState(2016);
  const [data, setData] = useState(null);
  const API = 'http://127.0.0.1:8000/api';

  const fetchData = () => {
    axios.get(`${API}/extra_runs_per_team/${year}/`).then(res => setData(res.data));
  };

  return (
    <Container sx={{mt:3}}>
      <h2>Extra runs conceded per team — Year</h2>
      <TextField label="Year" value={year} onChange={e=>setYear(e.target.value)} sx={{mr:2}} />
      <Button variant="contained" onClick={fetchData}>Fetch</Button>

      {data && (
        <ChartWrapper
          data={{
            labels: data.teams.map(t=>t.team),
            datasets:[{label:'Extra Runs', data:data.teams.map(t=>t.extra_runs)}]
          }}
          options={{plugins:{title:{display:true,text:`Extra runs conceded in ${data.year}`}}}}
        />
      )}
    </Container>
  );
}


// // frontend/src/pages/ExtraRuns.jsx
// import React, { useEffect } from "react";
// import axios from "axios";

// const ExtraRuns = () => {
//   useEffect(() => {
//     const API_BASE_URL = "http://127.0.0.1:8000/api";  // Django backend
//     axios.get(`${API_BASE_URL}/extra-runs/2016/`)
//       .then(response => {
//         console.log(response.data);
//       })
//       .catch(error => {
//         console.error(error);
//       });
//   }, []);

//   return (
//     <div>
//       <h1>Extra Runs Page</h1>
//       {/* You can render chart/data here */}
//     </div>
//   );
// };

// export default ExtraRuns;






// // Example: frontend/src/pages/ExtraRuns.jsx
// import axios from "axios";


// const API_BASE_URL = "http://127.0.0.1:8000/api";  // Django backend

// axios.get(`${API_BASE_URL}/extra-runs/2016/`)
//   .then(response => {
//     console.log(response.data);
//   })
//   .catch(error => {
//     console.error(error);
//   });

//  // Add this at the bottom
// export default ExtraRuns;








