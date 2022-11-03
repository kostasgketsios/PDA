<template>
  <v-app>
    <v-main>
      <v-row>
        <v-col>
          <v-btn v-on:click="handleClick('kafes1')"> Καφεδες </v-btn>
          <v-btn v-on:click="handleClick('anapsyktikas')"> Αναψυκτικα </v-btn>
          <v-btn v-on:click="handleClick('faghta')"> φαγητο </v-btn>
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
export default {
  created() {
    // if (
    //   this.$cookies.get("jwt") === null ||
    //   this.$cookies.get("jwt") === undefined
    // ) {
    //   window.location.href = "http://localhost:3000";
    // }
  },
  methods: {
    handleClick(value) {
      // console.log(value.id)
      let data = {
        pinakas: value,
      };
      this.$router.push({
        name: "proionta",
        params: { data },
      });
    },
  },
};
</script>

<style></style>
