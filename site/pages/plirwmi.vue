<template>
  <v-app>
    <v-main>
      <div class="text-center text-h4">
        <strong>Πληρωμή ειδών</strong>
      </div>
      <div class="text-center mt-5 text-h6">Σύνολο: {{ synolo }} &euro;</div>
      <div class="text-center mt-5">
        <v-row>
          <v-spacer></v-spacer>
          <v-col>
            <div class="text-subtitle-1">Πληκτρολόγησε το ποσό του πελάτη</div>
          </v-col>
          <v-col>
            <input
              placeholder="Ποσό πελάτη"
              type="number"
              v-model.number="posoPelati"
            />
          </v-col>
          <!-- <v-col>
            <div> {{ synolo }}</div>
          </v-col> -->
          <v-spacer></v-spacer>
        </v-row>
        <h2 class="text-center mt-12" v-if="result > 0" style="color: green">
          Ρέστα: {{ result }} &euro;
        </h2>
        <h2 class="text-center mt-12" style="color: red" v-else>
          Ρέστα: {{ result }} &euro;
        </h2>
      </div>
    </v-main>
  </v-app>
</template>
<script>
export default {
  name: "Login",
  data() {
    return {
      synolo: 0,
      posoPelati: "",
    };
  },
  computed: {
    result() {
      return this.posoPelati - this.synolo;
    },
  },
  created() {
    this.synolo = this.$route.params.poso;
  },
};
</script>
