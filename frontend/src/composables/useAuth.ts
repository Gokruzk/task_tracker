// src/composables/useAuth.ts
import { computed, ref } from 'vue'
import api from '@/api/axios'

const accessToken = ref(localStorage.getItem('access_token') || null)
const refreshToken = ref(localStorage.getItem('refresh_token') || null)

export function useAuth () {
  const login = async (username: string, password: string): Promise<boolean> => {
    try {
      const response = await api.post('/auth/login', {
        password,
        username,
      })

      const { access, refresh } = response.data

      accessToken.value = access
      refreshToken.value = refresh

      localStorage.setItem('access_token', access)
      localStorage.setItem('refresh_token', refresh)

      return true
    } catch (error) {
      console.error('Login error:', error)
      return false
    }
  }

  const register = async (username: string, password: string): Promise<boolean> => {
    try {
      await api.post('/auth/register', {
        password,
        username,
      })

      return true
    } catch (error) {
      console.error('Register error:', error)
      return false
    }
  }

  const logout = () => {
    accessToken.value = null
    refreshToken.value = null

    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
  }

  const isLoggedIn = computed(() => !!accessToken.value)

  return {
    accessToken,
    isLoggedIn,
    login,
    register,
    logout,
    refreshToken,
  }
}
