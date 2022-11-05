<template>
  <v-app>
    <v-main>
      <v-row>
        <v-col>
          <v-btn class="mt-4" block v-on:click="handleClick('kafedes')">
            Καφεδες
          </v-btn>
          <v-btn class="mt-4" block v-on:click="handleClick('anapsiktika')">
            Αναψυκτικα
          </v-btn>
          <v-btn class="mt-4" block v-on:click="handleClick('faghta')">
            φαγητο
          </v-btn>
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
import Vue from "vue";
import VueCookies from "vue-cookies";
export default {
  created() {},
  methods: {
    handleClick(value) {
      Vue.use(VueCookies);
      this.$cookies.set("pinakas", value, "5h");
      this.$router.push({
        name: "proionta",
      });
    },
  },
};
</script>

<style></style>
