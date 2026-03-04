// src/composables/useNotifications.ts
import { ref } from 'vue'

// ESTO DEBE ESTAR AFUERA (ESTADO COMPARTIDO)
const show = ref(false)
const message = ref('')
const color = ref('success')

export function useNotification () {
  const notify = (msg: string, type: 'success' | 'error' | 'info' = 'success') => {
    message.value = msg
    color.value = type
    show.value = true
  }

  return { show, message, color, notify }
}
