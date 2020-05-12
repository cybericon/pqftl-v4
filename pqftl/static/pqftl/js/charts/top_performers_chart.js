// Set new default font family and font color to mimic Bootstrap's default styling
(Chart.defaults.global.defaultFontFamily = "Nunito"),
  '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = "#858796";

// Bar Chart Example
var ctx = document.getElementById("top-performers");
var myBarChart = new Chart(ctx, {
  type: "horizontalBar",
  data: {
    labels: top_consultants,
    datasets: [
      {
        label: "Top 5 Consultants",
        backgroundColor: "#005B00",
        hoverBackgroundColor: "#8B0037",
        borderColor: "#005B00",
        data: top_consultants_business,
      },
    ],
  },
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 0,
        right: 5,
        top: 0,
        bottom: 0,
      },
    },
    legend: {
      display: false,
    },
    tooltips: {
      titleMarginBottom: 10,
      titleFontColor: "#6e707e",
      titleFontSize: 14,
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: "#dddfeb",
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
      callbacks: {},
    },
  },
});
