import { useEffect } from "@/lib/dom";
import { Chart } from "chart.js/auto";
import GameRoom from "./components/GameRoom";
import { NumberStepper } from "./components/Inputs";

const chartData = {
  day_of_week: [
    {
      day: "Sunday",
      count: 3,
      wins: 2,
    },
    {
      day: "Monday",
      count: 13,
      wins: 10,
    },
    {
      day: "Tuesday",
      count: 7,
      wins: 5,
    },
    {
      day: "Wednesday",
      count: 1,
      wins: 0,
    },
    {
      day: "Thursday",
      count: 4,
      wins: 2,
    },
    {
      day: "Friday",
      count: 10,
      wins: 9,
    },
    {
      day: "Saturday",
      count: 3,
      wins: 2,
    },
  ],
};

const TestPage = () => {
  // useEffect(() => {
  //   const labels = chartData.day_of_week.map((data) => {
  //     return data.day;
  //   });
  //   const numOfRound = chartData.day_of_week.map((data) => data.count);
  //   const numOfWins = chartData.day_of_week.map((data) => data.wins);
  //   const numOfLoses = chartData.day_of_week.map(
  //     (data) => data.count - data.wins
  //   );
  //   console.log(numOfRound, Math.max(...numOfRound));
  //   const rateOfWins = chartData.day_of_week.map((data) =>
  //     data.count ? (data.wins / data.count) * 100 : 0
  //   );
  //   console.log(labels);
  //   let ctx = document.getElementById("myChartCnt");
  //   new Chart(ctx, {
  //     data: {
  //       labels: labels,
  //       datasets: [
  //         {
  //           type: "bar",
  //           label: "Rounds",
  //           data: numOfRound,
  //           borderWidth: 1,
  //         },
  //         {
  //           type: "bar",
  //           label: "Win",
  //           data: numOfWins,
  //           borderWidth: 1,
  //         },
  //         {
  //           type: "bar",
  //           label: "Loses",
  //           data: numOfLoses,
  //           borderWidth: 1,
  //         },
  //       ],
  //     },
  //     options: {
  //       scales: {
  //         y: {
  //           grid: {
  //             color: (context) => {
  //               return "rgba(255,255,255,0.4)";
  //             },
  //           },
  //           beginAtZero: true,
  //         },
  //       },
  //     },
  //   });

  //   ctx = document.getElementById("myChartRate");
  //   new Chart(ctx, {
  //     data: {
  //       labels: labels,
  //       datasets: [
  //         {
  //           type: "line",
  //           tension: 0.3,
  //           label: "# of Votes",
  //           data: rateOfWins,
  //           borderWidth: 1,
  //           fill: true,
  //           backgroundColor: "rgba(255,255,255,0.3)",
  //         },
  //       ],
  //     },
  //     options: {
  //       scales: {
  //         y: {
  //           grid: {
  //             color: (context) => {
  //               // if (context.tick.value % 20 === 0) {
  //               //   return "rgba(255,255,255,0.8)";
  //               // }
  //               return "rgba(255,255,255,0.4)";
  //             },
  //             lineWidth: (context) => {
  //               return 1;
  //             },
  //           },
  //           ticks: {
  //             stepSize: 20,
  //           },
  //           beginAtZero: true,
  //         },
  //       },
  //     },
  //   });
  // }, []);
  return (
    <div class="test-game-main">
      <NumberStepper text="set score" type="input-goal" defaultValue={3} />
    </div>
  );
};

export default TestPage;
