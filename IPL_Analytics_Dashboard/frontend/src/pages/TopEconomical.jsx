import React, { useState } from "react";
import axios from "axios";
import ChartWrapper from "../components/ChartWrapper";
import { Container, TextField, Button } from "@mui/material";

export default function TopEconomical() {
  const [year, setYear] = useState(2016);
  const [data, setData] = useState(null);
  const API = "http://127.0.0.1:8000/api";

  const fetchData = async () => {
    try {
      const res = await axios.get(`${API}/top_economical_bowlers/${year}/`);
      setData(res.data);
    } catch (error) {
      console.error("Error fetching data:", error);
      alert("Failed to fetch data. Please check backend API URL.");
    }
  };

  return (
    <Container sx={{ mt: 3 }}>
      <h2>Top Economical Bowlers — Year</h2>
      <TextField
        label="Year"
        value={year}
        onChange={(e) => setYear(e.target.value)}
        sx={{ mr: 2 }}
      />
      <Button variant="contained" onClick={fetchData}>
        Fetch
      </Button>

      {data && data.bowlers && (
        <ChartWrapper
          data={{
            labels: data.bowlers.map((b) => b.bowler),
            datasets: [
              {
                label: "Economy",
                data: data.bowlers.map((b) => b.economy),
              },
            ],
          }}
          options={{
            plugins: {
              title: {
                display: true,
                text: `Top economical bowlers in ${data.year}`,
              },
            },
          }}
        />
      )}
    </Container>
  );
}




// import React, {useState} from 'react';
// import axios from 'axios';
// import ChartWrapper from '../components/ChartWrapper';
// import { Container, TextField, Button } from '@mui/material';

// export default function TopEconomical(){
//   const [year, setYear] = useState(2016);
//   const [data, setData] = useState(null);
//   const API = 'http://127.0.0.1:8000/api';

//   const fetchData = () => {
//     axios.get(`${API}/top-economical/${year}/?top=10`).then(res => setData(res.data));
//   };

//   return (
//     <Container sx={{mt:3}}>
//       <h2>Top Economical Bowlers — Year</h2>
//       <TextField label="Year" value={year} onChange={e=>setYear(e.target.value)} sx={{mr:2}} />
//       <Button variant="contained" onClick={fetchData}>Fetch</Button>

//       {data && (
//         <ChartWrapper
//           data={{
//             labels: data.bowlers.map(b=>b.bowler),
//             datasets:[{label:'Economy', data:data.bowlers.map(b=>b.economy)}]
//           }}
//           options={{plugins:{title:{display:true,text:`Top economical bowlers in ${data.year}`}}}}
//         />
//       )}
//     </Container>
//   );
// }
