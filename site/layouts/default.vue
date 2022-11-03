<template>
  <v-app>
    <AppHeader />
    <Nuxt />
  </v-app>
</template>

<script>
import AppHeader from "../components/inc/AppHeader.vue";
import Vue from "vue";
import VueCookies from "vue-cookies";

export default {
  components: { AppHeader },
  name: "DefaultLayout",
  data() {
    return {};
  },
  // mounted(){
  //     Vue.use(VueCookies);
  //     // console.log(this.$cookies.get("jwt"))

  //     if (this.$cookies.get("jwt") === null || this.$cookies.get("jwt") === undefined){
  //       console.log("Jwt Does Not Exists")
  //     }
  //     else{
  //       console.log("Jwt Does exist")
  //     }
  //   }
};
</script>
<style></style>

<!-- http://localhost:1337/api/restaurants?filters[categories][onoma][$eq]=nea -->
<!-- Ερώτημα για να φιλτράρω την απάντηση ανάλογα την κατήγορία που ανήκει η εγγραφή (ανακοίνωση η νεο;) -->
<!-- μπορώ να κάνω το ίδιο για οποιοδήποτε content type συσχετίσω στην εγγραφή -->

<!-- αν συνδεθεί ο χρήστης στην αρχική να μεταφέρεται το is logged in και αν είναι συνδεδεμένος να εμφανίζει το ονομα του η κάτι στη θέση του κουμπιού -->
\
<!-- Η αν δεν είναι null το jwt cookie -->
<!-- Να φτιάξω σελίδες για προσθήκη ανακοίνωσης -->
