import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Landing from './pages/Landing';
import ExtraRuns from './pages/ExtraRuns';
import TopEconomical from './pages/TopEconomical';
import MatchesPlayedVsWon from './pages/MatchesPlayedVsWon';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';

export default function App(){
  return (
    <>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>IPL Dashboard</Typography>
          <Button color="inherit" component={Link} to="/">Home</Button>
          <Button color="inherit" component={Link} to="/extra-runs">Extra Runs</Button>
          <Button color="inherit" component={Link} to="/top-economical">Top Economical</Button>
          <Button color="inherit" component={Link} to="/matches-played-vs-won">Played vs Won</Button>
        </Toolbar>
      </AppBar>
      <Routes>
        <Route path="/" element={<Landing/>} />
        <Route path="/extra-runs" element={<ExtraRuns/>} />
        <Route path="/top-economical" element={<TopEconomical/>} />
        <Route path="/matches-played-vs-won" element={<MatchesPlayedVsWon/>} />
      </Routes>
    </>
  );
}
