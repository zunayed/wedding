<template>
  <form>
    <label class="typo__label">Which events can you make it to?</label>
    <div
      v-for="event in Object.keys(eventLabels)"
      v-if="canView(event)"
      class="form-row align-i tems-center"
    >
      <div class="col-auto my-1">
        <span class="custom-control-description" v-text="`I am planning to go to ${eventLabels[event]}${canHaveGuests(event) ? ' with' : ''}`"></span>
      </div>
      <div v-if="canHaveGuests(event)" class="col-auto my-1">
        <select v-model="rsvp[event]" class="custom-select mr-sm-2" id="inlineFormCustomSelect">
          <option
            v-for="option in getGuestOptions(event)"
            v-bind:value="option.value"
            v-text="option.label"
          >
          </option>
        </select>
      </div>
      <span v-if="canHaveGuests(event)"> guest(s).</span>
    </div>
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
      holud: 0,
      wedding: 0,
      reception: 0,
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
        return doc.exists ? doc.data() : {
          holud: 0,
          wedding: 0,
          reception: 0,
        };
      });
    },
  },
};
</script>
