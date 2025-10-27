import React from "react";
import { Routes, Route, Link } from "react-router-dom";

import MatchesPerYear from "./pages/Landing"; // adjust import if needed
import ExtraRuns from "./pages/ExtraRuns";
import TopEconomical from "./pages/TopEconomical";
import MatchesPlayedVsWon from "./pages/MatchesPlayedVsWon";


function App() {
  return (
    <div>
      <header>
        <h1>IPL Dashboard</h1>
        <nav>
          <Link to="/">Home</Link> |{" "}
          
          <Link to="/extra_runs_per_team">Extra Runs</Link> |{" "}
          <Link to="/top_economical_bowlers">Top Economical Bowlers</Link> |{" "}
          <Link to="/matches-played-vs-won">Matches Played vs Won</Link>
        </nav>
      </header>

      <main>
        <Routes>
          <Route path="/" element={<MatchesPerYear />} />
          <Route path="/extra_runs_per_team" element={<ExtraRuns />} />
          <Route path="/top_economical_bowlers" element={<TopEconomical />} />
          <Route path="/matches-played-vs-won" element={<MatchesPlayedVsWon />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;


// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
