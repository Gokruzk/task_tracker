// src/components/login/loginService.ts
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '@/composables/useAuth'
import { useNotification } from '@/composables/useNotifications'

const error = ref('')
const loading = ref(false)

export function useLoginService () {
  const router = useRouter()
  const { login: authLogin } = useAuth()
  const { notify } = useNotification()

  async function login (username: string, password: string): Promise<boolean> {
    if (!username || !password) {
      error.value = 'Por favor, completa todos los campos'
      return false
    }

    loading.value = true
    error.value = ''

    try {
      const success = await authLogin(username, password)

      if (success) {
        notify('¡Bienvenido de nuevo!', 'success')

        await router.push('/tasks')

        return true
      } else {
        throw new Error('Credenciales incorrectas')
      }
    } catch (error_: any) {
      error.value = error_.response?.data?.detail || error_.message || 'Error al iniciar sesión'
      return false
    } finally {
      loading.value = false
    }
  }

  return {
    error,
    loading,
    login,
  }
}
