<template>
  <div class="home">
     <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: 'Home',
  
   mounted () {
    axios
      .get('http://127.0.0.1:8000/')
      .then(response => {
        console.log('test',response);
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
