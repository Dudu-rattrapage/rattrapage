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
  name: 'LineChart',
  props : ['entities'],
  methods: {
    reduceArray : function (arr) {
    var res =  [];
      for(let i=0;i<arr.length/2;i++){
          res.push(arr[i]);
      }
      return res;
    }
  },
   mounted () {
    var name_labels = this.entities.value.map(e=>e.domain);
    var pings = this.entities.value.map(e=>e.pings);
    // var timestamps = this.entities.value.map(e=>e.timestamps); 
    var times = []
    for(let i=0;i<this.entities.value[4].pings.length;i++){
        times.push(i);
    }
    console.log("entities",this.entities.value)
   
// {
                // label: name_labels[0],
                // data: pings[0],
                // backgroundColor: [
                //     'rgba(255, 99, 132, 0.2)',
                // ],
                // borderColor: [
                //     'rgba(255, 99, 132, 1)',
                // ]
                // },
                // {
                // label: name_labels[1],
                // data: pings[1],
                // backgroundColor: [
                //     'rgba(54, 162, 235, 0.2)',    
                // ],
                // borderColor: [
                //     'rgba(54, 162, 235, 1)',
                // ],
                // borderWidth: 1
                // },
                // {
                // label: name_labels[2],
                // data: pings[2],
                // backgroundColor: [         
                //     'rgba(255, 206, 86, 0.2)',
                // ],
                // borderColor: [
                //     'rgba(255, 206, 86, 1)',    
                // ],
                // borderWidth: 1
                // },
                // {
                // label: name_labels[3],
                // data: pings[3],
                // backgroundColor: [
                //     'rgba(75, 192, 192, 0.2)',     
                // ],
                // borderColor: [
                //     'rgba(75, 192, 192, 1)',  
                // ],
                // borderWidth: 1
                // },
    var ctx = document.getElementById("lineChart");
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: times.map(t=>t*5),
            datasets: [
                {
                label: name_labels[4],
                data: pings[4],
                backgroundColor: [         
                    'rgba(153, 102, 255, 0.2)',
                ],
                borderColor: [ 
                    'rgba(153, 102, 255, 1)',   
                ],
                borderWidth: 1
                },
                {
                label: name_labels[5],
                data: pings[5],
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
