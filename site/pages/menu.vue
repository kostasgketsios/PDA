<template>
  <v-app>
    <v-main>
      <v-row>
        <v-col>
          <v-btn class="mt-4" block v-on:click="handleClick"> προσθηκη </v-btn>
          <v-btn class="mt-4" block v-on:click="clear">
            Εκκαθαριση Τραπεζιου
          </v-btn>
        </v-col>
      </v-row>
      <v-data-table
        v-model="selected"
        :headers="headers"
        :items="this.proionta_apo_vasi"
        item-key="onoma"
        show-select
        class="elevation-1 mt-4"
      >
      </v-data-table>
      <v-btn dark color="#0c426f" class="mt-4" block v-on:click="print">
        Αποστολη παραγγελιας
      </v-btn>
    </v-main>
  </v-app>
</template>

<script>
import Vue from "vue";
import VueCookies from "vue-cookies";
export default {
  data() {
    return {
      data: {
        id: null,
        trapezi: null,
        pinakas: null,
        proion: null,
        timi: null,
      },
      proionta_apo_vasi: [],
      selected: [],
      headers: [
        { text: "Κατάσταση", value: "isPrinted" },
        {
          text: "Προϊόν",
          sortable: false,
          value: "onoma",
        },
        { text: "Τιμή", value: "timi" },
        { text: "Σερβιτόρος", value: "servitoros" },
        { text: "Ώρα", value: "wra" },
        // { text: "Protein (g)", value: "protein" },
        // { text: "Iron (%)", value: "iron" },
      ],
      // paraggelies: [],
    };
  },
  methods: {
    handleClick() {
      this.$router.push({
        name: "ab",
        // params: { data },
      });
    },
    print() {},
    clear() {
      var answer = confirm(
        "Είστε σίγουροι ότι θέλετε να διαγράψετε όλα τα προϊόντα από το τραπέζι: " +
          this.data.trapezi +
          ";"
      );
      if (answer) {
        const options = {
          method: "DELETE",
          headers: { "content-type": "application/json" },
          body: "false",
        };

        this.proionta_apo_vasi.forEach((element) => {
          console.log(element.id);
          fetch("http://localhost:1337/api/paraggelies/" + element.id, options)
            .then((response) => response.json())
            // .then((response) => console.log(response))
            .catch((err) => console.error(err));
        });
      }
      this.proionta_apo_vasi = [];
      const options = {
        method: "GET",
        headers: { "content-type": "application/json" },
      };

      setTimeout(() => {
        fetch(
          "http://localhost:1337/api/paraggelies?filters[arithmos_trapeziou][$eq]=" +
            this.data.trapezi,
          options
        )
          .then((response) => response.json())
          .then((response) =>
            response.data.forEach((element) => {
              console.log(element);
              this.proionta_apo_vasi.push({
                id: element.id,
                onoma: element.attributes.proion,
                timi: element.attributes.timi,
                servitoros: element.attributes.servitoros,
                isPrinted: element.attributes.isPrinted,
                wra: element.attributes.publishedAt.substring(11, 16),
              });
            })
          );
      }, 300);
    },
  },
  created() {
    Vue.use(VueCookies);

    if (this.$cookies.get("trapezi")) {
      this.data = {
        trapezi: this.$cookies.get("trapezi"),
        pinakas: null,
        proion: null,
        timi: null,
      };
    } else {
      this.data = {
        trapezi: this.$route.params.data.trapezi,
        pinakas: null,
        proion: null,
        timi: null,
      };
    }
    this.$root.$refs.AppHeader.setTrapezi(this.data.trapezi);
    const options = {
      method: "GET",
      headers: { "content-type": "application/json" },
    };
    fetch(
      "http://localhost:1337/api/paraggelies?filters[arithmos_trapeziou][$eq]=" +
        this.data.trapezi,
      options
    )
      .then((response) => response.json())
      .then((response) =>
        response.data.forEach((element) => {
          // console.log(element);
          this.proionta_apo_vasi.push({
            id: element.id,
            onoma: element.attributes.proion,
            timi: element.attributes.timi,
            servitoros: element.attributes.servitoros,
            isPrinted: element.attributes.isPrinted,
            wra: element.attributes.publishedAt.substring(11, 16),
          });
        })
      )
      .catch((err) => console.error(err));
  },
};
</script>
