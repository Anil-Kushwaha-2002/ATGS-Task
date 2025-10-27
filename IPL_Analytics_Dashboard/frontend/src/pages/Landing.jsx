import React, {useEffect, useState} from 'react';
import axios from 'axios';
import ChartWrapper from '../components/ChartWrapper';
import { Container, Box } from '@mui/material';

const API = 'http://127.0.0.1:8000/api';

export default function Landing(){
  const [matchesByYear, setMatchesByYear] = useState([]);
  const [stackData, setStackData] = useState(null);

  useEffect(()=>{
    axios.get(`${API}/matches-per-year/`).then(res => setMatchesByYear(res.data));
    axios.get(`${API}/wins-per-team-per-year/`).then(res => {
      // res: {seasons:[], teams:[], data: {season: [counts...]}}
      const {seasons, teams, data} = res.data;
      // data is keyed by season; convert to chartjs dataset
      const datasets = teams.map((team, idx) => ({
        label: team,
        data: seasons.map(s => data[s][idx]),
        stack: 'stack1'
      }));
      setStackData({ labels: seasons.map(String), datasets });
    });
  },[]);

  const matchesChart = {
    labels: matchesByYear.map(m => m.season),
    datasets: [{
      label: 'Matches',
      data: matchesByYear.map(m => m.matches)
    }]
  };
  const stackOptions = {
    responsive: true,
    plugins: { title: { display: true, text: 'Matches won — stacked by team per season' } },
    scales: { x: { stacked: true }, y: { stacked: true } }
  };

  return (
    <Container>
      <Box sx={{mt:3}}>
        <h2>Matches per Year</h2>
        <ChartWrapper data={{labels: matchesByYear.map(m=>m.season), datasets:[{label:'Matches', data:matchesByYear.map(m=>m.matches)}]}} options={{plugins:{title:{display:true,text:'Matches played per year'}}}} />
      </Box>

      <Box sx={{mt:5}}>
        <h2>Wins per Team (stacked) across seasons</h2>
        {stackData ? <ChartWrapper data={stackData} options={stackOptions} /> : <div>Loading...</div>}
      </Box>
    </Container>
  );
}
