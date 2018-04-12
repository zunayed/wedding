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
  data () {
    return {
      person: null,
      options: [],
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
      projectId: 'blog-741dd'
    });

    // Initialize Cloud Firestore through Firebase
    var db = firebase.firestore();
		var personDoc = db.collection("zu_rsvp").doc("Zunayed Ali");

		personDoc.get().then(function(doc) {
			if (doc.exists) {
				console.log("Document data:", doc.data());
			} else {
				// doc.data() will be undefined in this case
				console.log("No such document!");
			}
		}).catch(function(error) {
			console.log("Error getting document:", error);
		});

  },
}
</script>

<style>@import './assets/css/home.css'</style>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

