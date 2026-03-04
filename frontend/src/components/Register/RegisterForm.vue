<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" md="4" sm="8">
        <v-card :class="$style.card" elevation="8" rounded="lg">
          <v-card-title class="text-h5 font-weight-bold text-center">
            Registro de Usuario
          </v-card-title>

          <v-card-text>
            <v-form ref="registerForm" @submit.prevent="handleEmptySubmit">
              <v-text-field
                v-model="username"
                class="mb-2"
                label="Usuario"
                prepend-inner-icon="mdi-account"
                :rules="[rules.required]"
                variant="outlined"
              />

              <v-text-field
                v-model="password"
                class="mb-4"
                label="Contraseña"
                prepend-inner-icon="mdi-lock"
                :rules="[rules.required]"
                type="password"
                variant="outlined"
              />

              <v-btn
                block
                color="primary"
                :disabled="loading"
                :loading="loading"
                size="large"
                type="submit"
                variant="elevated"
              >
                Registrarse
              </v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-card-actions class="justify-center py-4">
      <span class="text-body-2 text-grey-darken-1">
        ¿Ya tienes una cuenta?
      </span>
      <v-btn class="text-none font-weight-bold ml-1" color="primary" to="/login" variant="text">
        Ingresa aquí
      </v-btn>
    </v-card-actions>
  </v-container>
</template>

<script setup lang="ts">
  import { nextTick, ref, watch } from 'vue'
  import { useNotification } from '@/composables/useNotifications'
  import { useRegisterService } from './RegisterService'

  const username = ref('')
  const password = ref('')
  const registerForm = ref<any>(null)

  const { register, loading, error } = useRegisterService()
  const { notify } = useNotification()

  const rules = {
    required: (value: string) => !!value || 'Este campo es obligatorio.',
  }

  watch(error, newError => {
    if (newError) {
      notify(newError, 'error')
    }
  })

  async function handleEmptySubmit () {
    const { valid } = await registerForm.value.validate()

    if (valid) {
      const success = await register(username.value, password.value)

      if (success) {
        notify('¡Registro exitoso!', 'success')

        await nextTick()
      }
    }
  }
</script>

<style module>
.card {
  padding: 24px;
}
</style>
