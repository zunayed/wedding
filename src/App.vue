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
					<div v-for="event in Object.keys(eventLabels)" class="form-row align-items-center">
						<div v-if="canView(event)" class="col-auto my-1">
							<span class="custom-control-description" v-text="`I am planning to go to ${eventLabels[event]}${canHaveGuests(event) ? ' with' : ''}`"></span>
						</div>

						<div v-if="canHaveGuests(event)" class="col-auto my-1">
							<select v-model="rsvp[event]" class="custom-select mr-sm-2" id="inlineFormCustomSelect">
                <option
                  v-for="option in getGuestOptions(event)"
                  v-bind:value="option.value">
                  {{ option.label }}
                </option>
							</select>
            </div>
            <span v-if="canHaveGuests(event)"> guest(s).</span>

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
import firestore 			from 'firebase';
import VueMultiselect from 'vue-multiselect';
import Papa           from 'papaparse';



import Calendar     	from "./sections/calendar.vue"


export default {
  name: 'app',
  components: {
    "calendar": Calendar,
    "multiselect": VueMultiselect,
  },
  data() {
    return {
      person: null,
      options: [],
    }
  },
  computed: {
    canViewHolud() {
      return this.canView('holud');
    },
    canViewWedding() {
      return this.canView('wedding');
    },
    canViewReception() {
      return this.canView('reception');
    }
  },
  created() {
    var csvData = null;

    Papa.parse('dist/wedding_list.csv', {
      header: true,
      download: true,
      complete: (results, file) => {
        console.log("Parsing complete:", results, file);
        this.options = results.data;
        console.log(this.options);
      }
    });


    firebase.initializeApp({
      apiKey: process.env.FB_KEY,
      authDomain: 'dtostillwell.com',
      projectId: 'blog-741dd',
    });

    // initialize attendees from canonical source
    // this.getCanonicalAttendees().then(attendees => {
    //   this.options = attendees;
    // });
  },
  methods: {
    canView(event) {
      return this.person[event] > 0;
    },
    canHaveGuests(event) {
      return this.person[event] > 1;
    },
    getRsvp(person) {
      return this.db.collection("zu_rsvp").doc(person.name).get().then(doc => {
        return doc.exists ? doc.data() : {
          holud: 0,
          wedding: 0,
          reception: 0,
        };
      }).then(rsvp => {
        console.log('rsvp for', person.name, rsvp);
        return rsvp;
      })
    },
    getCanonicalAttendees() {
      return Promise.resolve([
        { name: 'Kemal Gafar', holud: 1, wedding: 1, reception: 2 },
        { name: 'Shahbaz Shah', holud: 2, wedding: 2, reception: 2 },
        { name: 'Tasmiya Khan', holud: 2, wedding: 2, reception: 2 },
        { name: 'Sara Nik', holud: 2, wedding: 2, reception: 2 },
        { name: 'fob uncle', holud: 0, wedding: 0, reception: 2 },
      ]);
    },
    getGuestOptions(event) {
      const guestOptions = [
        {value: 0, label: 'Please select...'}
      ];
      for (let i = 1; i <= this.person[event]; i++) {
        guestOptions.push({value: i, label: i});
      }
      return guestOptions;
    }
  },
}
</script>

<style>@import './assets/css/home.css'</style>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

