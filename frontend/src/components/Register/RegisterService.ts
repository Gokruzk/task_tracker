// src/components/login/loginService.ts
import { ref } from 'vue'
import { useAuth } from '@/composables/useAuth'
import { useNotification } from '@/composables/useNotifications'

const error = ref('')
const loading = ref(false)

export function useRegisterService () {
  const { register: authRegister } = useAuth()
  const { notify } = useNotification()

  async function register (username: string, password: string): Promise<boolean> {
    if (!username || !password) {
      error.value = 'Por favor, completa todos los campos'
      return false
    }

    loading.value = true
    error.value = ''

    try {
      const success = await authRegister(username, password)

      if (success) {
        notify('¡Registro exitoso!', 'success')

        return true
      } else {
        throw new Error('Error al registrar')
      }
    } catch (error_: any) {
      error.value = error_.response?.data?.detail || error_.message || 'Error al registrar'
      return false
    } finally {
      loading.value = false
    }
  }

  return {
    error,
    loading,
    register,
  }
}
