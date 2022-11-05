<template>
  <v-app>
    <v-main>
      <v-toolbar dark color="#0c426f">
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
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      loading: false,
      items: [],
      search: null,
      select: null,
      states: [],
    };
  },
  watch: {
    search(val) {
      val && val !== this.select && this.querySelections(val);
    },
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
  },
  created() {
    const options = {
      method: "GET",
      headers: { "content-type": "application/json" },
    };

    fetch("http://localhost:1337/api/kafedes", options)
      .then((response) => response.json())
      .then((response) =>
        response.data.forEach((element) => {
          this.states.push(element.attributes.onoma);
        })
      )
      .catch((err) => console.error(err));
    fetch("http://localhost:1337/api/anapsiktika", options)
      .then((response) => response.json())
      .then((response) =>
        response.data.forEach((element) => {
          this.states.push(element.attributes.onoma);
        })
      )
      .catch((err) => console.error(err));
    fetch("http://localhost:1337/api/faghta", options)
      .then((response) => response.json())
      .then((response) =>
        response.data.forEach((element) => {
          this.states.push(element.attributes.onoma);
        })
      )
      .catch((err) => console.error(err));
  },
};
</script>
