from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
import firebase_admin as admin
import firebase_admin.auth as auth
import traceback


class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):

        token = request.headers.get('Authorization')
        print(token)
        if not token:
            return None
        try:
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token["uid"]
        except Exception:
            traceback.print_exc()
            return None
        try:
            user = User.objects.get(username=uid)
            return (user, True)
        except ObjectDoesNotExist:
            return None