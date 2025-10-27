import React from 'react';
import { Chart as ChartJS, BarElement, CategoryScale, LinearScale, Title, Tooltip, Legend } from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(BarElement, CategoryScale, LinearScale, Title, Tooltip, Legend);

export default function ChartWrapper({data, options}) {
  return <Bar data={data} options={options} />;
}




// import React from 'react';
// import { Chart as ChartJS, BarElement, CategoryScale, LinearScale, Title, Tooltip, Legend } from 'chart.js';
// import { Bar } from 'react-chartjs-2';

// ChartJS.register(BarElement, CategoryScale, LinearScale, Title, Tooltip, Legend);

// export default function ChartWrapper({ data, options }) {
//   // Default dark theme options
//   const darkOptions = {
//     plugins: {
//       legend: { labels: { color: "#ffffff" } },  // white legend text
//       title: { display: true, color: "#ffffff" }, // white title text
//       tooltip: { titleColor: "#ffffff", bodyColor: "#ffffff" },
//     },
//     scales: {
//       x: { ticks: { color: "#ffffff" }, grid: { color: "#444" } },
//       y: { ticks: { color: "#ffffff" }, grid: { color: "#444" } },
//     },
//     ...options, // allow overriding from props
//   };

//   return <Bar data={data} options={darkOptions} />;
// }


