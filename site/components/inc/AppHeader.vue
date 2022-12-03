<template>
  <v-container id="main-page">
    <v-app-bar color="#0c426f" dark clipped-left app>
      <v-app-bar-nav-icon @click="openClose(drawer)"></v-app-bar-nav-icon>
      <v-toolbar-title>PDA</v-toolbar-title>
      <v-spacer></v-spacer>

      <v-toolbar-title>Τραπέζι: {{ this.trapezi }}</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-toolbar-title>{{ this.proion }}</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-toolbar-title v-if="this.jwt" class="mr-3">{{
        this.username
      }}</v-toolbar-title>
      <v-toolbar-title v-else></v-toolbar-title>

      <v-btn v-if="this.jwt" @click="logout()" icon>
        <v-icon class="mr-3">mdi-logout</v-icon>
      </v-btn>

      <!-- <v-btn v-else icon to = "login">
                <v-icon class="mr-3">mdi-login</v-icon>
              </v-btn> -->
    </v-app-bar>
    <v-navigation-drawer clipped app v-model="drawer" permanent v-if="drawer">
      <v-list nav dense>
        <v-list-item-group active-class="#0c426f--text text--accent-4">
          <!-- να γινει textfield και στο place holder να βάλει το icon -->
          <v-list-item to="/search">
            <v-list-item-icon>
              <v-icon>mdi-magnify</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Αναζήτηση</v-list-item-title>
          </v-list-item>

          <v-list-item to="/home">
            <!-- to do history page -->
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Αρχική</v-list-item-title>
          </v-list-item>

          <v-list-item to="/history">
            <!-- to do history page -->
            <v-list-item-icon>
              <v-icon>mdi-history</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Ιστορικό παραγγελιών</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </v-container>
</template>
<script>
import Vue from "vue";
import VueCookies from "vue-cookies";

export default {
  name: "AppHeader",
  data: () => ({
    drawer: false,
    jwt: false,
    trapezi: null,
    proion: null,
    username: null,
  }),
  created() {
    this.$root.$refs.AppHeader = this;
  },
  beforeMount() {
    Vue.use(VueCookies);

    if (this.$cookies.get("jwt") !== null) {
      this.jwt = true;
    } else if (this.$cookies.get("jwt") !== null) {
      this.jwt = false;
    }
  },

  methods: {
    logout() {
      Vue.use(VueCookies);
      this.$cookies.remove("jwt");
      this.$cookies.remove("username");
      window.location.href = "http://localhost:8080";
    },

    openClose(drawer) {
      if (drawer === true) {
        this.drawer = false;
      } else {
        this.drawer = true;
      }
    },
    setTrapezi(arithmos) {
      this.trapezi = arithmos;
    },
    setProion(proion) {
      this.proion = proion;
    },
    setUsername(username) {
      this.username = username;
    },
    getUsername() {
      return this.username;
    },
  },
};
</script>
