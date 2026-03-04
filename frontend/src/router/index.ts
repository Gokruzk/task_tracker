// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import LoginForm from '@/components/Login/LoginForm.vue'
import RegisterForm from '@/components/Register/RegisterForm.vue'
import TasksView from '@/components/Tasks/TasksView.vue'
import { useAuth } from '@/composables/useAuth'

const routes = [
  { path: '/login', component: LoginForm, name: 'login' },
  { path: '/register', component: RegisterForm, name: 'register' },
  { path: '/tasks', component: TasksView, name: 'tasks', meta: { requiresAuth: true } },
  {
    path: '/',
    redirect: '/tasks',
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// Guard global
router.beforeEach((to, from, next) => {
  const { isLoggedIn } = useAuth()

  if (to.meta.requiresAuth && !isLoggedIn.value) {
    next({ name: 'login' })
  } else if (to.name === 'login' && isLoggedIn.value) {
    next({ name: 'tasks' })
  } else {
    next()
  }
})

export default router
