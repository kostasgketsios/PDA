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
      let data = {
        trapezi: null,
        pinakas: value,
        proion: null,
        timi: null,
      };
      if (this.$cookies.get("trapezi")) {
        data = {
          trapezi: this.$cookies.get("trapezi"),
          pinakas: value,
          proion: null,
          timi: null,
        };
      } else {
        data = {
          trapezi: this.$route.params.data.trapezi,
          pinakas: value,
          proion: null,
          timi: null,
        };
      }

      // this.$route.params.data.pinakas = value;
      this.$cookies.set("pinakas", value, "5h");
      this.$router.push({
        name: "proionta",
        params: { data },
      });
    },
  },
};
</script>

<style></style>
