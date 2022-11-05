<template>
  <v-app>
    <v-main>
      <v-row>
        <v-col>
          <span v-for="n in 11" :key="n">
            <v-btn v-on:click="handleClick(n)">
              {{ n }}
            </v-btn>
          </span>
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
import Vue from "vue";
import VueCookies from "vue-cookies";
export default {
  created() {
    if (
      this.$cookies.get("trapezi") !== null ||
      this.$cookies.get("trapezi") !== undefined
    ) {
      this.$cookies.remove("trapezi");
    }
    if (
      this.$cookies.get("proion") !== null ||
      this.$cookies.get("proion") !== undefined
    ) {
      this.$cookies.remove("proion");
    }
  },
  methods: {
    handleClick(n) {
      Vue.use(VueCookies);
      this.$cookies.set("trapezi", n, "5h");
      // let data = {
      //   trapezi: value,
      // };
      // this.$router.push({
      //   name: "ab",
      //   // params: { data },
      // });
      window.location.href = "http://localhost:3000/ab";
    },
  },
};
</script>

<style></style>
