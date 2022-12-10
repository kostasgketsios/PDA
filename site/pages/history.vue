<template>
  <v-app>
    <v-main>
      <v-data-table
        :headers="headers"
        :items="this.proionta_apo_vasi"
        item-key="id"
        show-select
        class="elevation-1 mt-4"
      >
      </v-data-table>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      proionta_apo_vasi: [],
      headers: [
        {
          text: "Προϊόν",
          sortable: false,
          value: "onoma",
        },
        // { text: "Τιμή", value: "timi" },
        { text: "Σερβιτόρος", value: "servitoros" },
        { text: "Ώρα", value: "wra" },
        { text: "Τραπέζι", value: "arithmos_trapeziou" },
        { text: "Σερβιτόρος", value: "servitoros" },
      ],
      // paraggelies: [],
    };
  },
  created() {
    const options = {
      method: "GET",
      headers: { "content-type": "application/json" },
    };
    fetch("http://localhost:1337/api/paraggelies", options)
      .then((response) => response.json())
      .then((response) =>
        response.data.forEach((element) => {
          this.proionta_apo_vasi.push({
            id: element.id,
            onoma: element.attributes.proion,
            timi: element.attributes.timi,
            servitoros: element.attributes.servitoros,
            isPrinted: element.attributes.isPrinted,
            wra: element.attributes.publishedAt.substring(11, 16),
            arithmos_trapeziou: element.attributes.arithmos_trapeziou,
          });
        })
      )
      .catch((err) => console.error(err));
  },
};
</script>
