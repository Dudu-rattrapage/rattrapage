<template>
    <div class="home">
        <div class="container">
            <canvas id="lineChart"></canvas>
        </div>
    </div>
</template>

<script>
import Chart from 'chart.js/auto';
export default {
  name: 'Home',
  data(){
    return {
        labels : ['Home router', 'Plex media', 'SFR TV', 'Nvidia Shield', 'DNS Google', 'Riot Games'],
        pings : [12, 19, 3, 5, 2, 3],
        timeStamps : [1,2,3,4,5,6,7,8]
    }
  },
   mounted () {
    var ctx = document.getElementById("lineChart");
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: this.timeStamps ,
            datasets: [{
                label: this.labels[0],
                data: this.pings,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                ]
                },
                {
                label: this.labels[1],
                data: this.pings[1],
                backgroundColor: [
                    'rgba(54, 162, 235, 0.2)',    
                ],
                borderColor: [
                    'rgba(54, 162, 235, 1)',
                ],
                borderWidth: 1
                },
                {
                label: this.labels[2],
                data: this.pings[2],
                backgroundColor: [         
                    'rgba(255, 206, 86, 0.2)',
                ],
                borderColor: [
                    'rgba(255, 206, 86, 1)',    
                ],
                borderWidth: 1
                },
                {
                label: this.labels[3],
                data: this.pings[3],
                backgroundColor: [
                    'rgba(75, 192, 192, 0.2)',     
                ],
                borderColor: [
                    'rgba(75, 192, 192, 1)',  
                ],
                borderWidth: 1
                },
                {
                label: this.labels[4],
                data: this.pings[4],
                backgroundColor: [         
                    'rgba(153, 102, 255, 0.2)',
                ],
                borderColor: [ 
                    'rgba(153, 102, 255, 1)',   
                ],
                borderWidth: 1
                },
                {
                label: this.labels[5],
                data: this.pings[5],
                backgroundColor: [
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
                }   
            ]
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
