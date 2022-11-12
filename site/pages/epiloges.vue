<template>
  <v-app>
    <v-main>
      <v-snackbar v-model="snackbar" absolute top right color="success">
        <span>Το προϊόν προστέθηκε στο καλάθι</span>
        <v-icon dark> mdi-checkbox-marked-circle </v-icon>
      </v-snackbar>
      <v-form ref="form" @submit.prevent="submit">
        <v-row>
          <v-col>
            <v-row>
              <v-col></v-col>
              <v-col class="ml-11">
                <p>Ποσότητα</p>
              </v-col>
              <v-col>
                <v-btn
                  dark
                  color="#0c426f"
                  class="mr-4 ml-12"
                  v-on:click="handleClick('dec')"
                  >-</v-btn
                >
                {{ this.counter }}
                <v-btn
                  dark
                  color="#0c426f"
                  class="ml-4"
                  v-on:click="handleClick('inc')"
                  >+</v-btn
                >
              </v-col>
              <v-col></v-col>
            </v-row>
            <div v-if="this.$cookies.get('pinakas') === 'kafedes'">
              <v-row>
                <v-col></v-col>
                <v-col class="ml-11">
                  <p>Ποσότητα ζάχαρης</p>
                </v-col>
                <v-col>
                  <div class="">
                    <v-select
                      @change="add('posotita_zaxaris', $event)"
                      v-model="form.posotita_zaxaris"
                      :items="posotites_zaxaris"
                      color="#0c426f"
                      label="Ποσότητα ζάχαρης"
                      required
                    >
                    </v-select>
                  </div>
                </v-col>
                <v-col></v-col>
              </v-row>
              <v-row>
                <v-col></v-col>
                <v-col class="ml-11">
                  <p>Είδος ζάχαρης</p>
                </v-col>
                <v-col
                  ><div class="">
                    <v-select
                      @change="add('eidos_zaxaris', $event)"
                      :items="eidos_zaxaris"
                      color="#0c426f"
                      label="Είδος ζάχαρης"
                      required
                    >
                    </v-select></div
                ></v-col>
                <v-col></v-col>
              </v-row>
              <v-row>
                <v-col></v-col>
                <v-col class="ml-11">
                  <p>Γάλα</p>
                </v-col>
                <v-col
                  ><div class="">
                    <v-select
                      @change="add('gala', $event)"
                      :items="gala"
                      color="#0c426f"
                      label="Ποσότητα Γάλατος"
                      required
                    >
                    </v-select></div
                ></v-col>
                <v-col></v-col>
              </v-row>
              <v-row>
                <v-col></v-col>
                <v-col class="ml-11">
                  <p>Κανέλα</p>
                </v-col>
                <v-col
                  ><div class="">
                    <v-select
                      @change="add('kanela', $event)"
                      :items="kanela"
                      color="#0c426f"
                      label="Κανέλα"
                      required
                    >
                    </v-select></div
                ></v-col>
                <v-col></v-col>
              </v-row>
            </div>
            <div v-if="this.$cookies.get('pinakas') === 'faghta'">
              <v-row>
                <v-col></v-col>
                <v-col class="ml-11">
                  <p>Επιλογές Φαγητών</p>
                </v-col>
                <v-col>
                  <div class="">
                    <v-select
                      @change="add('faghta', $event)"
                      :items="faghta"
                      color="#0c426f"
                      label="Επιλογές"
                      :multiple="true"
                      required
                    >
                    </v-select>
                  </div>
                </v-col>
                <v-col>
                </v-col>
              </v-row>
            </div>
          </v-col>
        </v-row>
        <v-row>
          <v-col></v-col>
          <v-col class="ml-11">
            <v-text-field
              counter="50"
              label="Σχόλια"
              @change="add('sxolia', $event)"
            ></v-text-field>
          </v-col>
          <v-col></v-col>
        </v-row>
        <v-row>
          <v-col class="ml-11">
            <div style="text-align: center">
              <v-btn
                dark
                :disabled="!formIsValid"
                color="#0c426f"
                type="submit"
              >
                Προσθηκη
              </v-btn>
            </div>
          </v-col>
        </v-row>
      </v-form>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    const defaultForm = Object.freeze({
      posotita_zaxaris: "",
      eidos_zaxaris: "",
      gala: "",
      kanela: "",
      faghta: "",
    });
    return {
      form: Object.assign({}, defaultForm),
      counter: 1,
      proion_gia_kalathi: {
        posotita_zaxaris: "Σκέτος",
        eidos_zaxaris: "Λευκή",
        gala: "Χωρίς γάλα",
        kanela: "Χωρίς γάλα",
        faghta: "Χωρίς πιπεριά",
        sxolia: "",
        posotita: this.counter,
      },
      posotites_zaxaris: [
        "Σκέτος",
        "Ολίγη",
        "Μέτριος",
        "Μέτριος προς Γλυκό",
        "Γλυκός",
        "Πολύ Γλυκός",
      ],
      eidos_zaxaris: ["Λευκή", "Καστανή", "Στέβια", "ζαχαρίνη"],
      gala: ["Με γάλα", "Χωρίς Γάλα", "Πολύ Γάλα", "Λίγο Γάλα"],
      kanela: ["Με κανέλα", "Χωρίς κανέλα"],
      faghta: [
        "Με πιπεριές",
        "Χωρίς πιπεριές",
        "Με μανιτάρια",
        "Χωρίς μανιτάρια",
        "Με κρεμύδια",
        "Χωρίς κρεμύδια",
      ],
      snackbar: false,
      proion: [],
    };
  },
  computed: {
    formIsValid() {
        if (this.$cookies.get("faghta")) {
        return true;
      } else {
        return this.form.posotita_zaxaris;
      }
    },
//    formIsValid() {
 //     this.$router.push({
  //      name: "menu",
   //   });
   // },
  },
  methods: {
    add(epilogh, event) {
      this.$cookies.set(epilogh, event, "5h");
    },
    handleClick(upDown) {
      if (upDown === "inc") {
        this.counter = this.counter + 1;
      } else if (upDown === "dec") {
        this.counter = this.counter - 1;
      }
    },
    submit() {
      this.snackbar = true;
      this.proion_gia_kalathi.posotita = this.counter;
      this.proion_gia_kalathi.posotita_zaxaris = this.$cookies.get("posotita_zaxaris");
      this.proion_gia_kalathi.eidos_zaxaris = this.$cookies.get("eidos_zaxaris");
      this.proion_gia_kalathi.gala = this.$cookies.get("gala");
      this.proion_gia_kalathi.kanela = this.$cookies.get("kanela");
      this.proion_gia_kalathi.faghta = this.$cookies.get("faghta");
      this.proion_gia_kalathi.sxolia = this.$cookies.get("sxolia");

      this.resetForm();

      this.$cookies.remove("posotita_zaxaris");
      this.$cookies.remove("eidos_zaxaris");
      this.$cookies.remove("gala");
      this.$cookies.remove("kanela");
      this.$cookies.remove("faghta");
      this.$cookies.remove("sxolia");
    },
    resetForm() {
      this.form = Object.assign({}, this.defaultForm);
      this.counter = 1;
      this.$refs.form.reset();
    },
  },
};
</script>

<style></style>

<!-- σε cookie (αν γίνεται να αποθηκεύσω αντικείμενο)
μαλλον json.stringify -->
