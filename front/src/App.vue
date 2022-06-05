<template>
<div>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  <Modale v-bind:display="display"/>
  <BarChart/>
  <LineChart/>
</div>
</template>

<script>
import axios from "axios";
import BarChart from './components/BarChart.vue'
import LineChart from './components/LineChart.vue'
import Modale from "./components/Modal.vue"

export default {
name: 'App',
components: {
    BarChart,
    LineChart,
    Modale
},
data(){
    return {
        display : false,

    }
},
mounted () {
    axios.get('http://127.0.0.1:8000/')
    .then(response => {
        console.log('test',response);
    });
}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
