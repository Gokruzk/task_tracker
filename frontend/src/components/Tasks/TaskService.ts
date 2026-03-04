import api from '@/api/axios'

export interface TaskStatus {
  code: string
  id: string
}

export interface Task {
  created_at: string
  description: string
  id: string
  status: TaskStatus
  title: string
}

export const taskService = {
  create: (data: any) =>
    api.post('/tasks', data),

  delete: (id: string) =>
    api.delete(`/tasks/${id}`),

  getStatuses: () =>
    api.get('/status'),

  list: (params: any) =>
    api.get('/tasks', { params }),

  update: (id: string, data: any) =>
    api.put(`/tasks/${id}`, data),
}
