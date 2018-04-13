<template>
  <form>
    <label class="typo__label">Which events can you make it to?</label>
    <div
      v-for="event in Object.keys(eventLabels)"
      v-if="canView(event)"
      class="form-row align-items-center"
    >
      <div class="col-auto" v-html="eventLabels[event]"></div>

      <div class="col-auto">
        <div class="btn-group" role="group" aria-label="Basic example"></div>
        <button type="button" v-on:click="setCanAttend(event, false)" v-bind:class="`btn btn-${rsvp[event].canAttend ? 'secondary': 'primary'}`">I can’t make it!</button>
        <button type="button" v-on:click="setCanAttend(event, true)" v-bind:class="`btn btn-${rsvp[event].canAttend ? 'primary': 'secondary'}`">I’ll be attending</button>
      </div>
      <div v-if="rsvp[event].canAttend" class="col-auto my-1">
        <p>The total number of guest attending including myself is</p>
        <select v-model="rsvp[event].total" class="custom-select mr-sm-2" id="inlineFormCustomSelect">
          <option
            v-for="option in getGuestOptions(event)"
            v-bind:value="option.value"
            v-text="option.label"
          >
          </option>
        </select>
      </div>
    </div>
    <br/>
    <button type="submit" class="btn btn-primary my-1">Send RSVP</button>
  </form>
</template>

<script>
import firestore from 'firebase'

export default {
  data: () => ({
    eventLabels: {
      holud: 'Gaye Holud',
      wedding: 'Nikkah',
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
  }),
  props: [
    'person'
  ],
  watch: {
    person(value) {
      if (value) {
        this.getRsvp(value).then(rsvp => {
          this.rsvp = rsvp;
        });
      }
    },
  },
  created() {
    this.db = firebase.app().firestore();
  },
  methods: {
    setCanAttend(event, canAttend) {
      console.log('clicked', event, canAttend);
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
  },
};
</script>
