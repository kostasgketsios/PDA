<template>
  <v-app>
    <v-main>
      <v-row>
        <v-col>
          <span v-for="n in 11" :key="n">
            <v-btn
              class="ml-5 mb-2"
              :id="n"
              :color="color"
              v-on:click="handleClick(n)"
              style="height: 100px; width: 100px"
            >
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
  data() {
    return {
      color: null,
      proionta_apo_vasi: [],
    };
  },
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
    const options = {
      method: "GET",
      headers: { "content-type": "application/json" },
    };
    fetch("http://localhost:1337/api/paraggelies", options)
      .then((response) => response.json())
      .then((response) => {
        if (response.data !== null) {
          response.data.forEach((element) => {
            this.proionta_apo_vasi.push({
              arithmos_trapeziou: element.attributes.arithmos_trapeziou,
              isReadyToPrint: element.attributes.readyToPrint,
              isPrinted: element.attributes.isPrinted,
            });
          });
        }
        this.proionta_apo_vasi.forEach((element) => {
          if (
            element.isPrinted &&
            document.getElementById(element.arithmos_trapeziou).style
              .backgroundColor === ""
          ) {
            document.getElementById(
              element.arithmos_trapeziou
            ).style.backgroundColor = "green";
          }
          if (!element.isReadyToPrint) {
            document.getElementById(
              element.arithmos_trapeziou
            ).style.backgroundColor = "red";
          }
        });
      })
      .catch((err) => console.error(err));
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
      //window.location.href = "http://localhost:3000/menu";

      let data = {
        trapezi: n,
        pinakas: null,
        proion: null,
        timi: null,
      };
      this.$router.push({
        name: "menu",
        params: { data },
      });
      // window.location.href = "http://localhost:3000/ab";
    },
  },
};
</script>

<style></style>
