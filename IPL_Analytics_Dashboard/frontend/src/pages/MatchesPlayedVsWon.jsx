import React, {useState} from 'react';
import axios from 'axios';
import { Container, TextField, Button } from '@mui/material';
import { Bar } from 'react-chartjs-2';

export default function MatchesPlayedVsWon(){
  const [year, setYear] = useState(2016);
  const [data, setData] = useState(null);
  const API = 'http://127.0.0.1:8000/api';

  const fetchData = () => {
    axios.get(`${API}/matches-played-vs-won/${year}/`).then(res => setData(res.data));
  };

  const formatData = () => {
    const labels = data.data.map(d => d.team);
    return {
      labels,
      datasets:[
        {label:'Played', data: data.data.map(d=>d.played), stack: 's1'},
        {label:'Won', data: data.data.map(d=>d.won), stack: 's1'},
      ]
    };
  };

  return (
    <Container sx={{mt:3}}>
      <h2>Matches Played vs Won — Year</h2>
      <TextField label="Year" value={year} onChange={e=>setYear(e.target.value)} sx={{mr:2}} />
      <Button variant="contained" onClick={fetchData}>Fetch</Button>

      {data && <Bar data={formatData()} options={{plugins:{title:{display:true,text:`Played vs Won in ${data.year}`}}}} />}
    </Container>
  );
}
