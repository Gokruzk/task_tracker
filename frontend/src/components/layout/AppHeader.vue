<template>
  <v-app-bar v-if="isLoggedIn" color="primary" elevation="2">
    <v-app-bar-title class="font-weight-bold">
      Task Manager
    </v-app-bar-title>

    <v-spacer />

    <v-btn class="mr-4" prepend-icon="mdi-logout" variant="text" @click="handleLogout">
      Cerrar Sesión
    </v-btn>
  </v-app-bar>
</template>

<script setup lang="ts">
  import { useRouter } from 'vue-router'
  import { useAuth } from '@/composables/useAuth'
  import { useNotification } from '@/composables/useNotifications'

  const router = useRouter()
  const { isLoggedIn, logout } = useAuth()
  const { notify } = useNotification()

  function handleLogout () {
    logout()
    notify('Sesión cerrada correctamente', 'info')
    router.push('/login')
  }
</script>
