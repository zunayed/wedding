<template>
  <div class="container" id="app">
    <br/>

    <div class="section row">

      <div class="col-sm-12">
        <img class="img-fluid" src="dist/images/top.png">
      </div>

    </div>
    <div class="section row">

      <div class="col-sm-12">
        <img class="img-fluid" src="dist/images/us.png">
      </div>

    </div>

    <hr/>
    <br/>

    <div class="section row">
      <div class="col-sm-12">

        <div class="alert alert-success" role="alert">
          <h4 class="alert-heading">Please RSVP!</h4>
          <p>Thanks for visiting our wedding website! Please take a second to rsvp for the events! If you don't see your name reach out to us email:zunayed@gmail.com</p>

          <hr>

          <p class="mb-0">
            <label class="typo__label">What's your name?</label>
            <multiselect
              v-model="person"
              :options="options"
              :custom-label="nameWithNickName"
              track-by="name">
            </multiselect>

            <div v-if="person">
              <br/>
              <rsvp-form :person="person"></rsvp-form>
            </div>
          </p>
        </div>

        <hr>

        <calendar :person="person"></calendar>

      </div>
    </div>

  </div>
</template>

<script>
import firestore 			from 'firebase';
import VueMultiselect from 'vue-multiselect';
import Papa           from 'papaparse';



import Calendar     	from "./sections/calendar.vue"
import RsvpForm       from "./sections/rsvp-form.vue"

export default {
  name: 'app',
  components: {
    "calendar": Calendar,
    "multiselect": VueMultiselect,
    "rsvp-form": RsvpForm,
  },
  data() {
    return {
      person: null,
      options: [],
    }
  },
  created() {
    firebase.initializeApp({
      apiKey: process.env.FB_KEY,
      authDomain: 'dtostillwell.com',
      projectId: 'blog-741dd',
    });
    // initialize attendees from canonical source
    this.getWeddingList().then(attendees => {
      this.options = attendees;
    });
  },
  methods: {
    getWeddingList() {
      return new Promise(resolve => Papa.parse('dist/wedding_list.csv', {
        header: true,
        download: true,
        complete: results => resolve(results.data),
      }));
    },
    nameWithNickName ({ name, nickname }) {
      if (!nickname) {
        return name;
      }

      return `${name} — [${nickname}]`
    }
  }
}
</script>

<style>@import './assets/css/home.css'</style>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

