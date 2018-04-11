<template>
  <div class="container" id="app">
    <br/>

    <div class="section row">

      <div class="col-12">
         <img class="img-fluid" src="dist/images/us.png">
      </div>

    </div>

    <hr/>
    <br/>
	<calendar></calendar>

	<div class="alert alert-success" role="alert">
	  <h4 class="alert-heading">Please RSVP!</h4>
	  <p>Thanks for visiting our wedding website! Please take a second to rsvp for the events! If you don't see your name reach out to us email:zunayed@gmail.com</p>
	  <hr>
	  <p class="mb-0">ll</p>
	</div>


  </div>
</template>

<script>
import Calendar  from "./sections/Calendar.vue"


export default {
  name: 'app',
  components: {
	"calendar": Calendar,
  },
}
</script>

<style>@import './assets/css/home.css'</style>
