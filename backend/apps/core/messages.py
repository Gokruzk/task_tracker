from rest_framework import status

APP_MESSAGES = {
    "successfully_retrieved": {
        "status_code": status.HTTP_200_OK,
        "detail": "Datos obtenidos correctamente",
    },
    "task_created": {
        "status_code": status.HTTP_201_CREATED,
        "detail": "Tarea creada correctamente",
    },
    "no_tasks_found": {
        "status_code": status.HTTP_404_NOT_FOUND,
        "detail": "No se encontraron tareas",
    },
    "unexpected_error": {
        "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
        "detail": "Ocurrió un error inesperado",
    },
    "invalid_credentials": {
        "status_code": status.HTTP_401_UNAUTHORIZED,
        "detail": "Credenciales inválidas",
    },
}
