// Set new default font family and font color to mimic Bootstrap's default styling
(Chart.defaults.global.defaultFontFamily = "Nunito"),
  '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = "#858796";

function number_format(number, decimals, dec_point, thousands_sep) {
  // *     example: number_format(1234.56, 2, ',', ' ');
  // *     return: '1 234,56'
  number = (number + "").replace(",", "").replace(" ", "");
  var n = !isFinite(+number) ? 0 : +number,
    prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
    sep = typeof thousands_sep === "undefined" ? "," : thousands_sep,
    dec = typeof dec_point === "undefined" ? "." : dec_point,
    s = "",
    toFixedFix = function (n, prec) {
      var k = Math.pow(10, prec);
      return "" + Math.round(n * k) / k;
    };
  // Fix for IE parseFloat(0.55).toFixed(0) = 0;
  s = (prec ? toFixedFix(n, prec) : "" + Math.round(n)).split(".");
  if (s[0].length > 3) {
    s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
  }
  if ((s[1] || "").length < prec) {
    s[1] = s[1] || "";
    s[1] += new Array(prec - s[1].length + 1).join("0");
  }
  return s.join(dec);
}

// Area Chart Example
var ctx = document.getElementById("business-trend");
var myLineChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "Jun",
      "Jul",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec",
    ],
    datasets: [
      {
        label: business_trend[0].branch,
        lineTension: 0.3,
        backgroundColor: "rgba(0, 91, 0, 1)",
        fill: false,
        borderColor: "rgba(0, 91, 0, 1)",
        pointRadius: 3,
        pointBackgroundColor: "rgba(0, 91, 0, 1)",
        pointBorderColor: "rgba(0, 91, 0, 1)",
        pointHoverRadius: 3,
        pointHoverBackgroundColor: "rgba(0, 91, 0, 1)",
        pointHoverBorderColor: "rgba(0, 91, 0, 1)",
        pointHitRadius: 10,
        pointBorderWidth: 2,
        data: business_trend[0].business,
      },
      {
        label: business_trend[1].branch,
        lineTension: 0.3,
        backgroundColor: "rgba(34, 124, 157, 1)",
        fill: false,
        borderColor: "rgba(34, 124, 157, 1)",
        pointRadius: 3,
        pointBackgroundColor: "rgba(34, 124, 157, 1)",
        pointBorderColor: "rgba(34, 124, 157, 1)",
        pointHoverRadius: 3,
        pointHoverBackgroundColor: "rgba(34, 124, 157, 1)",
        pointHoverBorderColor: "rgba(34, 124, 157, 1)",
        pointHitRadius: 10,
        pointBorderWidth: 2,
        data: business_trend[1].business,
      },
      {
        label: business_trend[2].branch,
        lineTension: 0.3,
        backgroundColor: "rgba(48, 99, 142, 1)",
        fill: false,
        borderColor: "rgba(48, 99, 142, 1)",
        pointRadius: 3,
        pointBackgroundColor: "rgba(48, 99, 142, 1)",
        pointBorderColor: "rgba(48, 99, 142, 1)",
        pointHoverRadius: 3,
        pointHoverBackgroundColor: "rgba(48, 99, 142, 1)",
        pointHoverBorderColor: "rgba(48, 99, 142, 1)",
        pointHitRadius: 10,
        pointBorderWidth: 2,
        data: business_trend[2].business,
      },
      {
        label: business_trend[3].branch,
        lineTension: 0.3,
        backgroundColor: "rgba(165, 64, 45, 1)",
        fill: false,
        borderColor: "rgba(165, 64, 45, 1)",
        pointRadius: 3,
        pointBackgroundColor: "rgba(165, 64, 45, 1)",
        pointBorderColor: "rgba(165, 64, 45, 1)",
        pointHoverRadius: 3,
        pointHoverBackgroundColor: "rgba(165, 64, 45, 1)",
        pointHoverBorderColor: "rgba(165, 64, 45, 1)",
        pointHitRadius: 10,
        pointBorderWidth: 2,
        data: business_trend[3].business,
      },
      {
        label: business_trend[4].branch,
        lineTension: 0.3,
        backgroundColor: "rgba(139, 0, 55, 1)",
        fill: false,
        borderColor: "rgba(139, 0, 55, 1)",
        pointRadius: 3,
        pointBackgroundColor: "rgba(139, 0, 55, 1)",
        pointBorderColor: "rgba(139, 0, 55, 1)",
        pointHoverRadius: 3,
        pointHoverBackgroundColor: "rgba(139, 0, 55, 1)",
        pointHoverBorderColor: "rgba(139, 0, 55, 1)",
        pointHitRadius: 10,
        pointBorderWidth: 2,
        data: business_trend[4].business,
      },
    ],
  },
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 10,
        right: 25,
        top: 25,
        bottom: 0,
      },
    },
    scales: {
      xAxes: [
        {
          time: {
            unit: "date",
          },
          gridLines: {
            display: false,
            drawBorder: false,
          },
          ticks: {
            maxTicksLimit: 7,
          },
        },
      ],
      yAxes: [
        {
          ticks: {
            maxTicksLimit: 5,
            padding: 10,
            // Include a dollar sign in the ticks
            callback: function (value, index, values) {
              return "PKR" + number_format(value);
            },
          },
          gridLines: {
            color: "rgb(234, 236, 244)",
            zeroLineColor: "rgb(234, 236, 244)",
            drawBorder: false,
            borderDash: [2],
            zeroLineBorderDash: [2],
          },
        },
      ],
    },
    legend: {
      display: true,
      position: "bottom",
      padding: 20,
    },
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      titleMarginBottom: 10,
      titleFontColor: "#6e707e",
      titleFontSize: 14,
      borderColor: "#dddfeb",
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      intersect: false,
      mode: "index",
      caretPadding: 10,
      callbacks: {
        label: function (tooltipItem, chart) {
          var datasetLabel =
            chart.datasets[tooltipItem.datasetIndex].label || "";
          return datasetLabel + ": PKR" + number_format(tooltipItem.yLabel);
        },
      },
    },
  },
});
