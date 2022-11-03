<template>
  <v-app>
    <v-main>
      <v-row>
        <v-col>
          <v-btn
            v-for="(item, index) in proionta"
            :key="index"
            style="white-space: pre-wrap"
            >{{ item.onoma }} --- {{ item.timi }}</v-btn
          >
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
import Vue from "vue";
import VueCookies from "vue-cookies";

export default {
  props: ["pinakas"],
  data() {
    return {
      proionta: [],
    };
  },
  mounted() {
    let data = this.$route.params.data.pinakas;
    // if (
    //   this.$cookies.get("pinakas") !== null ||
    //   this.$cookies.get("pinakas") !== undefined
    // ) {
    //   data = this.$cookies.get("pinakas");
    // }
    const options = {
      method: "GET",
      headers: { "content-type": "application/json" },
    };

    fetch("http://localhost:1337/api/" + data, options)
      .then((response) => response.json())
      .then((response) =>
        response.data.forEach((element) => {
          // console.log(element);
          let ant = {
            onoma: element.attributes.onoma,
            timi: element.attributes.timi,
            id: element.id,
          };

          this.proionta.push(ant);
        })
      )
      .catch((err) => console.error(err));
    this.$cookies.set("pinakas", data, "5h");
  },
  destroyed() {
    this.$cookies.remove("pinakas");
  },
  created() {},
};
</script>

<style></style>
