import logging
import requests
from rest_framework.permissions import BasePermission

from apps.repositories import ProfileRepo
log = logging.getLogger(__file__)
class CustomAuthenticated(BasePermission):
    def has_permission(self, request, view):
        try:
            repo = ProfileRepo()
            token = request.headers.get("Authorization")
            if not token:
                return False
            token = token.split(" ")[1] if "Bearer" in token else token
            profile = repo.verify_user_by_token(token=token)

            if profile:
                request.user = profile
                request.token = token
                return True
            return False
        except Exception as e:
            log.error(str(e))