<template>
  <v-container
    class="py-8"
    fluid
  >
    <v-row
      align="center"
      justify="center"
    >
      <v-col cols="12">
        <v-card
          elevation="2"
          rounded="lg"
        >
          <v-card-title class="d-flex align-center justify-space-between py-4">
            <div class="d-flex align-center">
              <span class="text-h5 font-weight-bold mr-4">Tareas</span>
              <v-btn
                color="primary"
                prepend-icon="mdi-plus"
                variant="elevated"
                @click="openCreate"
              >
                Nueva Tarea
              </v-btn>
            </div>

            <v-btn-toggle
              v-model="statusFilter"
              color="primary"
              density="comfortable"
              mandatory
              variant="outlined"
              @update:model-value="onFilterChange"
            >
              <v-btn value="">Todas</v-btn>

              <v-btn v-for="st in statuses" :key="st.id" :value="st.id">
                {{ st.code }}
              </v-btn>
            </v-btn-toggle>
          </v-card-title>

          <v-divider />

          <v-data-table-server
            v-model:items-per-page="itemsPerPage"
            v-model:page="page"
            :headers="headers"
            item-value="id"
            :items="tasks"
            :items-length="totalItems"
            :loading="loading"
            @update:options="fetchTasks"
          >
            <template #[`item.status`]="{ item }">
              <v-chip
                :color="getStatusColor(item.status.code)"
                label
                size="small"
                variant="flat"
              >
                {{ item.status.code }}
              </v-chip>
            </template>

            <template #[`item.actions`]="{ item }">
              <v-btn
                class="mr-2"
                icon="mdi-pencil"
                size="small"
                variant="text"
                @click="openEdit(item)"
              />
              <v-btn
                color="error"
                icon="mdi-delete"
                size="small"
                variant="text"
                @click="deleteTask(item.id)"
              />
            </template>
          </v-data-table-server>
        </v-card>
      </v-col>
    </v-row>

    <v-dialog
      v-model="dialog"
      max-width="500"
      persistent
    >
      <v-card rounded="lg">
        <v-card-title class="pa-4">
          {{ editedItem.id ? 'Editar Tarea' : 'Nueva Tarea' }}
        </v-card-title>

        <v-divider />

        <v-card-text class="pa-4">
          <v-form
            ref="taskForm"
            @submit.prevent="handleSave"
          >
            <v-text-field
              v-model="editedItem.title"
              class="mb-2"
              label="Título"
              :rules="[v => !!v || 'Requerido']"
              variant="outlined"
            />

            <v-textarea
              v-model="editedItem.description"
              class="mb-2"
              label="Descripción"
              rows="3"
              variant="outlined"
            />

            <v-select
              v-model="editedItem.status"
              class="mb-2"
              item-title="code"
              item-value="id"
              :items="statuses"
              label="Estado"
              :rules="[v => !!v || 'Requerido']"
              variant="outlined"
            />
          </v-form>
        </v-card-text>

        <v-card-actions class="pa-4">
          <v-spacer />
          <v-btn
            color="grey"
            variant="text"
            @click="dialog = false"
          >
            Cancelar
          </v-btn>
          <v-btn
            color="primary"
            :loading="formLoading"
            variant="elevated"
            @click="handleSave"
          >
            Guardar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script setup lang="ts">
  import { onMounted, ref } from 'vue'
  import { useTasks } from '@/composables/useTasks'

  const taskForm = ref<any>(null)
  const {
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
  } = useTasks()

  const headers = [
    { title: 'Título', key: 'title', align: 'start' as const },
    { title: 'Estado', key: 'status', align: 'center' as const },
    { title: 'Acciones', key: 'actions', align: 'end' as const, sortable: false },
  ]

  onMounted(() => fetchStatuses())

  function onFilterChange () {
    page.value = 1
    fetchTasks()
  }

  async function handleSave () {
    const { valid } = await taskForm.value.validate()
    if (valid) await saveTask()
  }

  function getStatusColor (code: string) {
    const colors: any = { PENDING: 'warning', IN_PROGRESS: 'info', COMPLETED: 'success' }
    return colors[code]
  }
</script>
