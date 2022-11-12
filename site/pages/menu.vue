<template>
   <v-app>
        <v-main>
            <v-row>
                <v-col>
                    <v-btn class="mt-4" block v-on:click="handleClick">
                       προσθηκη
                    </v-btn> 
                    <v-btn class="mt-4" block v-on:click="clear">
                      Εκκαθαριση Τραπεζιου
                   </v-btn>             
                </v-col>
            </v-row>
        </v-main>
   </v-app>
</template>

<script>
import Vue from "vue";
import VueCookies from "vue-cookies";
export default {
  created() {},
  methods: {
    handleClick() {
      Vue.use(VueCookies);
      this.$router.push({
        name: "ab",
      });  
    },
  },
};
</script>