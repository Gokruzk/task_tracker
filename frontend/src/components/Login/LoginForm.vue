<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" md="4" sm="8">
        <v-card :class="$style.card" elevation="8" rounded="lg">
          <v-card-title class="text-h5 font-weight-bold text-center">
            Iniciar sesión
          </v-card-title>

          <v-card-text>
            <v-form ref="loginForm" @submit.prevent="handleEmptySubmit">
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
                Ingresar
              </v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <v-card-actions class="justify-center py-4">
      <span class="text-body-2 text-grey-darken-1">
        ¿Aún no tienes una cuenta?
      </span>
      <v-btn class="text-none font-weight-bold ml-1" color="primary" to="/register" variant="text">
        Regístrate aquí
      </v-btn>
    </v-card-actions>
  </v-container>
</template>

<script setup lang="ts">
  import { nextTick, ref, watch } from 'vue'
  import { useNotification } from '@/composables/useNotifications'
  import { useLoginService } from './LoginService'

  // 1. Estado local
  const username = ref('')
  const password = ref('')
  const loginForm = ref<any>(null)

  // 2. Composables
  const { login, loading, error } = useLoginService()
  const { notify } = useNotification()

  // 3. Reglas de validación
  const rules = {
    required: (value: string) => !!value || 'Este campo es obligatorio.',
  }

  // 4. Observador de errores del servicio
  watch(error, newError => {
    if (newError) {
      notify(newError, 'error')
    }
  })

  // 5. Lógica de envío
  async function handleEmptySubmit () {
    const { valid } = await loginForm.value.validate()

    if (valid) {
      const success = await login(username.value, password.value)

      if (success) {
        // Esta notificación sobrevivirá al cambio de ruta porque vive en App.vue
        notify('¡Bienvenido de nuevo!', 'success')

        // Esperamos a que Vue procese el cambio de 'show = true'
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
