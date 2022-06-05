<template>
    <div class="home">
        <div class="container">
            <canvas id="barChart"></canvas>
        </div>
    </div>
</template>

<script>
import Chart from 'chart.js/auto';
export default {
  name: 'BarChart',
  data(){
    return {
        labels : ['Home router', 'Plex media', 'SFR TV', 'Nvidia Shield', 'DNS Google', 'Riot Games'],
        datas : [12, 19, 3, 5, 2, 3],
    }
  },
   mounted () {
    var ctx = document.getElementById("barChart");
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: this.labels ,
            datasets: [{
                label: this.labels,
                data: this.datas,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
                }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                }
            }
        }
    });
    myChart;
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.countainer{
    width: 50%;
    margin:auto;
}
</style>
