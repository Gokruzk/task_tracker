import { ref } from 'vue'
import { type Task, taskService, type TaskStatus } from '@/components/Tasks/TaskService'
import { useNotification } from './useNotifications'

export function useTasks () {
  const { notify } = useNotification()

  // --- Estado de Tabla ---
  const itemsPerPage = ref(10)
  const loading = ref(false)
  const page = ref(1)
  const statusFilter = ref('')
  const tasks = ref<Task[]>([])
  const totalItems = ref(0)

  // --- Estado de CRUD ---
  const defaultItem = { title: '', description: '', status: '' }
  const dialog = ref(false)
  const editedItem = ref<any>({ ...defaultItem })
  const formLoading = ref(false)
  const statuses = ref<TaskStatus[]>([])

  /**
   * Carga las tareas desde el backend aplicando paginación y filtros
   */
  async function fetchTasks () {
    loading.value = true
    try {
      const params = {
        page: page.value,
        page_size: itemsPerPage.value,
        status: statusFilter.value || undefined,
      }

      // Llamamos a la función list pasándole los parámetros
      const { data } = await taskService.list(params)

      tasks.value = data.results.data
      totalItems.value = data.count
    } catch {
      notify('Error al cargar tareas', 'error')
    } finally {
      loading.value = false
    }
  }

  /**
   * Carga el catálogo de estados disponibles
   */
  async function fetchStatuses () {
    try {
      const { data } = await taskService.getStatuses()
      // Asignamos directamente la data (el array de estados)
      statuses.value = data
    } catch (error) {
      console.error('Error cargando estados:', error)
    }
  }

  const openCreate = () => {
    editedItem.value = { ...defaultItem }
    dialog.value = true
  }

  const openEdit = (item: Task) => {
    // Mapeamos el ID del status para que el v-select lo reconozca
    editedItem.value = {
      ...item,
      status: item.status.id,
    }
    dialog.value = true
  }

  /**
   * Guarda o actualiza una tarea
   */
  async function saveTask () {
    formLoading.value = true
    try {
      if (editedItem.value.id) {
        await taskService.update(editedItem.value.id, editedItem.value)
        notify('Tarea actualizada', 'success')
      } else {
        await taskService.create(editedItem.value)
        notify('Tarea creada', 'success')
      }
      dialog.value = false
      await fetchTasks()
    } catch {
      notify('Error al guardar', 'error')
    } finally {
      formLoading.value = false
    }
  }

  /**
   * Elimina una tarea por su ID
   */
  async function deleteTask (id: string) {
    if (!confirm('¿Eliminar tarea?')) {
      return
    }

    try {
      await taskService.delete(id)
      notify('Tarea eliminada', 'success')
      await fetchTasks()
    } catch {
      notify('Error al eliminar', 'error')
    }
  }

  // --- Retorno en Orden Alfabético ---
  return {
    deleteTask,
    dialog,
    editedItem,
    fetchStatuses,
    fetchTasks,
    formLoading,
    itemsPerPage,
    loading,
    openCreate,
    openEdit,
    page,
    saveTask,
    statusFilter,
    statuses,
    tasks,
    totalItems,
  }
}
