<template>
  <div class="container" id="app">
    <br/>

    <div class="section row">

      <div class="col-12">
         <img class="img-fluid" src="dist/images/top.png">
      </div>

    </div>
    <div class="section row">

      <div class="col-12">
         <img class="img-fluid" src="dist/images/us.png">
      </div>

    </div>

    <hr/>
    <br/>

	<div class="alert alert-success" role="alert">
	  <h4 class="alert-heading">Please RSVP!</h4>
    <p>Thanks for visiting our wedding website! Please take a second to rsvp for the events! If you don't see your name reach out to us email:zunayed@gmail.com</p>

    <hr>

    <p class="mb-0">
      <label class="typo__label">What's your name?</label>
      <multiselect
        v-model="person"
        :options="options"
        label="name"
        track-by="name">
      </multiselect>


      <div v-if="person">
        <br/>
        <label class="typo__label">Which events can you make it to?</label>

				<form>
					<div class="form-row align-items-center">
						<div class="col-auto my-1">
							<div class="custom-control mr-sm-2">
								<input type="checkbox" class="custom-control-input">
								<label class="custom-control-label">I am planning to go to Gay holud with</label>
							</div>
						</div>

						<div class="col-auto my-1">
							<select class="custom-select mr-sm-2" id="inlineFormCustomSelect">
								<option selected>Please select...</option>
                <option v-for="num in [1, 2, 3]">{{ num }}</option>
							</select>
            </div>

            guest(s).

					</div>
				</form>

				<form>
					<div class="form-row align-items-center">
						<div class="col-auto my-1">
							<div class="custom-control mr-sm-2">
								<input type="checkbox" class="custom-control-input">
								<label class="custom-control-label">I am planning to go to Gay holud with</label>
							</div>
						</div>

						<div class="col-auto my-1">
							<select class="custom-select mr-sm-2" id="inlineFormCustomSelect">
								<option selected>Please select...</option>
                <option v-for="num in [1, 2, 3]">{{ num }}</option>
							</select>
            </div>

            guest(s).

					</div>
				</form>

        <br/>
        <button type="submit" class="btn btn-primary my-1">Send RSVP</button>


      </div>
    </p>
	</div>

  <hr>

	<calendar :person="person"></calendar>

  </div>
</template>

<script>
import VueMultiselect from 'vue-multiselect';

import Calendar     from "./sections/calendar.vue"

export default {
  name: 'app',
  components: {
    "calendar": Calendar,
    "multiselect": VueMultiselect,
  },
  data () {
    return {
      person: null,
      options: [
        { name: 'Kemal Gafar', holud: 1, wedding: 1, reception: 2 },
        { name: 'Shahbaz Shah', holud: 2, wedding: 2, reception: 2 },
        { name: 'Tasmiya Khan', holud: 2, wedding: 2, reception: 2 },
        { name: 'Sara Nik', holud: 2, wedding: 2, reception: 2 },
        { name: 'fob uncle', holud: 0, wedding: 0, reception: 2 },
      ]
    }
  },
  computed: {
    canViewHolud() {
      return this.person.holud > 0;
    },
    canViewWedding() {
      return this.person.wedding > 0;
    },
    canViewReception() {
      return this.person.reception > 0;
    }
  },

}
</script>

<style>@import './assets/css/home.css'</style>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

