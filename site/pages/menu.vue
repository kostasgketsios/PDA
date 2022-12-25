<template>
  <v-app>
    <v-main>
      <v-snackbar v-model="snackbar" absolute top right color="success">
        <span>Το προϊόν εκτυπώθηκε επιτυχώς</span>
        <v-icon dark> mdi-checkbox-marked-circle </v-icon>
      </v-snackbar>
      <v-snackbar
        v-model="snackbarFail"
        absolute
        top
        right
        color="red accent-2"
      >
        <span
          >Κάτι πήγε στραβά παρακαλώ δοκιμάστε πάλι η επικοινωνήστε με τον
          διαχειριστή</span
        >
        <v-icon dark> mdi-cancel </v-icon>
      </v-snackbar>
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
        item-key="id"
        show-select
        class="elevation-1 mt-4"
      >
      </v-data-table>
      <p v-if="this.synolo" class="text-center">
        <strong>Σύνολο: {{ this.synolo }} &euro;</strong>
      </p>
      <v-btn dark color="#0c426f" class="mt-4" block v-on:click="print">
        Αποστολη παραγγελιας
      </v-btn>
      <v-btn dark color="#0c426f" class="mt-4" block v-on:click="pay">
        Πληρωμή Ειδών
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
      success: false,
      snackbar: false,
      snackbarFail: false,
      data: {
        id: null,
        trapezi: null,
        pinakas: null,
        proion: null,
        timi: null,
      },
      proionta_apo_vasi: [],
      selected: [],
      synolo: null,
      headers: [
        { text: "Κατάσταση", value: "isPrinted" },
        {
          text: "Προϊόν",
          sortable: false,
          value: "onoma",
        },
        { text: "Τιμή", value: "timi" },
        // { text: "Σερβιτόρος", value: "servitoros" },
        // { text: "Ώρα", value: "wra" },

        // { text: "Protein (g)", value: "protein" },
        // { text: "Iron (%)", value: "iron" },
      ],
      // paraggelies: [],
    };
  },
  methods: {
    reloadItems() {
      const options = { method: "GET" };
      this.synolo = 0;
      this.selected.forEach((element) => {
        fetch(
          "http://localhost:1337/api/paraggelies?filters[arithmos_trapeziou][$eq]=" +
            this.data.trapezi +
            "&filters[isPrinted][$eq]=true&filters[id][$eq]=" +
            element.id,
          options
        )
          .then((response) => response.json())
          .then((response) =>
            // console.log(response)
            {
              if (response.data[0] === undefined) {
                this.snackbarFail = true;
              } else if (response.data[0].attributes.isPrinted) {
                this.snackbar = true;
                this.success = true;
                element.isPrinted = "Εκτυπωμένο";
                this.synolo = this.synolo + parseFloat(element.timi);
              }
              console.log(this.synolo);
            }
          )
          .catch((err) => console.error(err));
      });
      this.selected = [];
    },
    handleClick() {
      this.$router.push({
        name: "ab",
        // params: { data },
      });
    },
    pay() {
      let poso = this.synolo;
      this.$router.push({
        name: "plirwmi",
        params: { poso },
      });
    },
    print() {
      if (this.selected.length === 0) {
        this.selected = this.proionta_apo_vasi;
      }

      this.selected.forEach((element) => {
        const options = {
          method: "PUT",
          headers: { "content-type": "application/json" },
          body: '{"data":{"readyToPrint":true}}',
        };

        fetch("http://localhost:1337/api/paraggelies/" + element.id, options)
          .then((response) => response.json())
          .catch((err) => console.error(err));
      });
      setTimeout(() => {
        this.reloadItems();
      }, 300);
    },
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
          fetch("http://localhost:1337/api/paraggelies/" + element.id, options)
            .then((response) => response.json())
            .then((response) => console.log(response))
            .catch((err) => console.error(err));
        });
        this.synolo = null;
      }
      this.proionta_apo_vasi = [];
      const options = {
        method: "GET",
        headers: { "content-type": "application/json" },
      };
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
          let kat = null;
          if (element.attributes.isPrinted) {
            kat = "Εκτυπωμένο";
            this.synolo = this.synolo + parseFloat(element.attributes.timi);
          } else {
            kat = "Αναμονή για εκτύπωση";
          }
          this.proionta_apo_vasi.push({
            id: element.id,
            onoma:
              element.attributes.proion +
              " " +
              element.attributes.sxolia.replace(/null/g, " "),
            timi: element.attributes.timi,
            servitoros: element.attributes.servitoros,
            isPrinted: kat,
            wra: element.attributes.publishedAt.substring(11, 16),
          });
        })
      )
      .catch((err) => console.error(err));
  },
};
</script>
