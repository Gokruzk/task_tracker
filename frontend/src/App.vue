<template>
  <v-app>
    <AppHeader />

    <v-main>
      <router-view />
    </v-main>

    <v-snackbar v-model="show" :color="color" location="top" :timeout="3000">
      {{ message }}

      <template #actions>
        <v-btn icon="mdi-close" variant="text" @click="show = false" />
      </template>
    </v-snackbar>
  </v-app>
</template>

<script setup lang="ts">
  import AppHeader from '@/components/layout/AppHeader.vue'
  import { useNotification } from './composables/useNotifications'

  const { color, message, show } = useNotification()
</script>
