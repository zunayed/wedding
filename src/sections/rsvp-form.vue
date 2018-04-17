<template>
  <form>
    <label class="typo__label">Which events can you make it to?</label>
    <div
      v-for="event in Object.keys(eventLabels)"
      v-if="canView(event)"
      class="form-row align-items-center"
      >
      <div class="col-2">
        <b>{{ eventLabels[event] }}</b>
      </div>

      <div class="col-auto">
        <div class="btn-group" role="group" aria-label="Basic example"></div>
        <button type="button" v-on:click="setCanAttend(event, false)" v-bind:class="`btn btn-${rsvp[event].canAttend ? 'secondary': 'primary'}`">I can’t make it!</button>
        <button type="button" v-on:click="setCanAttend(event, true)" v-bind:class="`btn btn-${rsvp[event].canAttend ? 'primary': 'secondary'}`">I’ll be attending</button>
      </div>
      <br/>
      <div v-if="rsvp[event].canAttend" class="col-auto my-1">
        <p>The total number of guest attending including myself is
        <select v-model="rsvp[event].total" class="custom-select mr-sm-2" id="inlineFormCustomSelect">
          <option
            v-for="option in getGuestOptions(event)"
            v-bind:value="option.value"
            v-text="option.label"
            >
          </option>
        </select>
      </p>
      </div>
    <br/>
    </div>
    <br/>
    <button v-on:click.prevent="setRsvp" class="btn btn-primary my-1">Send/Update RSVP</button>

    <br/>
    <br/>

    <transition name="fade">
      <div v-if="sentResponse "class="alert alert-primary" role="alert">
        We have recorded rsvp response! Thanks!
      </div>
    </transition>

  </form>
</template>

<script>
import firestore from 'firebase'

export default {
  data: () => ({
    eventLabels: {
      holud: 'Gaye Holud',
      wedding: 'Wedding',
      reception: 'Reception',
    },
    rsvp: {
      holud: {
        canAttend: false,
        total: 0,
      },
      wedding: {
        canAttend: false,
        total: 0,
      },
      reception: {
        canAttend: false,
        total: 0,
      },
    },
    sentResponse: false,
    failRequest: false,
  }),
  props: [
    'person'
  ],
  watch: {
    person(value) {
      this.sentResponse = false;

      if (value) {
        this.getRsvp(value).then(rsvp => {
          this.rsvp = rsvp;
        });
      }
    },
  },
  created() {
    this.db = firebase.app().firestore();
    this.getRsvp(this.person).then(rsvp => {
      this.rsvp = rsvp;
    });
  },
  methods: {
    setCanAttend(event, canAttend) {
      this.rsvp[event].canAttend = canAttend;
    },
    canView(event) {
      return this.person[event] > 0;
    },
    canHaveGuests(event) {
      return this.person[event] > 1;
    },
    getGuestOptions(event) {
      const guestOptions = [
        {value: 0, label: 'Please select...'}
      ];
      for (let i = 1; i <= this.person[event]; i++) {
        guestOptions.push({value: i, label: i});
      }
      return guestOptions;
    },
    getRsvp(person) {
      return this.db.collection("zu_rsvp").doc(person.name).get().then(doc => {
        if (!doc.exists) {
          return {
            holud: {
              total: 0,
              canAttend: false,
            },
            wedding: {
              total: 0,
              canAttend: false,
            },
            reception: {
              total: 0,
              canAttend: false,
            },
          }
        };

        const rsvp = doc.data();
        console.info(doc.data());
        this.sentResponse = true;

        return {
          holud: {
            total: rsvp.holud,
            canAttend: rsvp.holud > 0,
          },
          wedding: {
            total: rsvp.wedding,
            canAttend: rsvp.wedding > 0,
          },
          reception: {
            total: rsvp.reception,
            canAttend: rsvp.reception > 0,
          },
        };

      });
    },
    setRsvp() {
      this.db.collection("zu_rsvp").doc(this.person.name).set({
          holud: this.rsvp.holud.total,
          wedding: this.rsvp.wedding.total,
          reception: this.rsvp.reception.total,
      })
        .then( () => {
        console.log("Document successfully written!");
        this.sentResponse = true;

      })
      .catch(function(error) {
        console.error("Error writing document: ", error);
        this.failRequest = true;
      });
    }
  },
};
</script>

<style>
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
