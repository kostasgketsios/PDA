<template>
  <v-app>
    <v-main>
      <v-data-table
        :headers="headers"
        :items="this.antikeim"
        :items-per-page="5"
        sort-by="id"
        :sort-desc="true"
      >
      </v-data-table>
    </v-main>
  </v-app>
</template>

<script>
export default {
  async mounted() {
    // Kanonika tha krataei istoriko twra gia epeidiksi exei kafedes
    const response = await fetch("http://localhost:1337/api/kafes1");
    const data = await response.json();
    const ant = [];
    data.data.forEach((element) => {
      let antikeimeno = {
        id: element.id,
        onoma: element.attributes.onoma,
        timi: element.attributes.timi,
      };
      ant.push(antikeimeno);
    });
    this.antikeim = ant;
    // this.antikeim = ant;
  },
  //   props: ["antikeim"],

  data() {
    return {
      antikeim: [],

      headers: [
        {
          text: "Τίτλος",
          align: "start",
          sortable: true,
          value: "onoma",
        },
        { text: "Λεπτομέρειες", value: "timi" },
        // to value tha prepei na exei ta onomata pou exw kai san pedia sto antikeimeno
      ],
    };
  },
};
</script>
