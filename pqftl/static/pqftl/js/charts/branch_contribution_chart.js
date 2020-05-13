// Set new default font family and font color to mimic Bootstrap's default styling
(Chart.defaults.global.defaultFontFamily = "Nunito"),
  '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = "#858796";
let raw_data = business;
let new_data = raw_data.map((value) => {
  const arrSum = (arr) => arr.reduce((a, b) => a + b, 0);
  sum = arrSum(raw_data);
  return Math.round((value / sum) * 100);
});

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: branches,
    datasets: [
      {
        data: new_data,
        backgroundColor: [
          "#005B00",
          "#227C9D",
          "#30638E",
          "#A5402D",
          "#8B0037",
        ],
        hoverBackgroundColor: [
          "#64AD59",
          "#71BECE",
          "#85B1C7",
          "#D29078",
          "#C56B93",
        ],
        hoverBorderColor: "rgba(234, 236, 244, 1)",
      },
    ],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: "#dddfeb",
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: true,
      caretPadding: 10,
    },
    legend: {
      display: true,
      position: "bottom",
    },
    cutoutPercentage: 50,
    circumference: Math.PI,
    rotation: -Math.PI,
  },
});
