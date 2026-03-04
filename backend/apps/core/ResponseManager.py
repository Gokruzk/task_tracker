# apps/core/response_manager.py
from rest_framework.response import Response
from .messages import APP_MESSAGES


class ResponsesManager:
    @staticmethod
    def success(message_key: str, data=None):
        msg = APP_MESSAGES.get(message_key, APP_MESSAGES["unexpected_error"])
        resp = {"success": True, "message": msg["detail"]}
        if data is not None:
            resp["data"] = data
        return Response(resp, status=msg["status_code"])

    @staticmethod
    def error(message_key: str):
        msg = APP_MESSAGES.get(message_key, APP_MESSAGES["unexpected_error"])
        resp = {"success": False, "message": msg["detail"], "data": None}
        return Response(resp, status=msg["status_code"])
