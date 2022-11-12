<template>
  <v-app>
    <v-main>
      <v-row style="margin-top: -36px">
        <v-col>
          <v-toolbar dark color="#0c426f" class="elevation-5">
            <v-toolbar-title>Αναζήτηση</v-toolbar-title>
            <v-autocomplete
              v-model="select"
              :loading="loading"
              :items="items"
              :search-input.sync="search"
              cache-items
              class="mx-4"
              flat
              hide-no-data
              hide-details
              label="Πληκτρολογήστε για αναζήτηση"
              solo-inverted
            ></v-autocomplete>
            <v-btn icon>
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </v-toolbar>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-btn
            class="mt-4"
            block
            v-for="(item, index) in proionta"
            :key="index"
            style="white-space: pre-wrap"
            v-on:click="handleClick(item.onoma, item.timi)"
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
      loading: false,
      items: [],
      search: null,
      select: null,
      states: [],
      proionta: [],
    };
  },
  watch: {
    search(val) {
      val && val !== this.select && this.querySelections(val);
    },
  },
  mounted() {
    Vue.use(VueCookies);
    let pinakas = null;
    if (this.$cookies.get("pinakas")) {
      pinakas = this.$cookies.get("pinakas");
    } else {
      pinakas = this.$route.params.data.pinakas;
    }
    // pinakas = this.$cookies.get("pinakas");
    const options = {
      method: "GET",
      headers: { "content-type": "application/json" },
    };

    fetch("http://localhost:1337/api/" + pinakas, options)
      .then((response) => response.json())
      .then((response) =>
        response.data.forEach((element) => {
          let ant = {
            onoma: element.attributes.onoma,
            timi: element.attributes.timi,
            id: element.id,
          };

          this.proionta.push(ant);
        })
      )
      .catch((err) => console.error(err));
  },
  methods: {
    querySelections(v) {
      this.loading = true;
      // Simulated ajax query
      this.items = this.states.filter((e) => {
        return (e || "").toLowerCase().indexOf((v || "").toLowerCase()) > -1;
      });
      this.loading = false;
    },
    // handleclick2() {
    //   window.location.href = "http://localhost:3000/epiloges";
    // },
    handleClick(onoma, timi) {
      Vue.use(VueCookies);
      let data = {
        trapezi: null,
        pinakas: null,
        proion: onoma,
        timi: timi,
      };
      if (this.$cookies.get("trapezi") && this.$cookies.get("pinakas")) {
        data = {
          trapezi: this.$cookies.get("trapezi"),
          pinakas: this.$cookies.get("pinakas"),
          proion: onoma,
          timi: timi,
        };
      } else {
        data = {
          trapezi: this.$route.params.data.trapezi,
          pinakas: this.$route.params.data.pinakas,
          proion: onoma,
          timi: timi,
        };
      }

      // this.$route.params.data.onoma = onoma;
      // this.$route.params.data.timi = timi;

      this.$cookies.set("proion", onoma, "5h");
      this.$cookies.set("timi", timi, "5h");

      this.$router.push({
        name: "epiloges",
        params: { data },
      });
      // window.location.href = "http://localhost:3000/epiloges";
    },
  },
  destroyed() {},
  created() {
    let pinakas = null;
    const options = {
      method: "GET",
      headers: { "content-type": "application/json" },
    };
    if (this.$cookies.get("pinakas")) {
      pinakas = this.$cookies.get("pinakas");
    } else {
      pinakas = this.$route.params.data.pinakas;
    }
    fetch("http://localhost:1337/api/" + pinakas, options)
      .then((response) => response.json())
      .then((response) =>
        response.data.forEach((element) => {
          this.states.push(element.attributes.onoma);
        })
      );
  },
};
</script>

<style></style>
