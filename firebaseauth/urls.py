from django.urls import path, re_path
#from rest_framework.urlpatterns import format_suffix_format
from firebaseauth import views
from .views.login import Login
from .views.register import Register
from .views.delete import DeleteUser

register = Register.as_view({'get':'list','post':'create'})
login = Login.as_view({'get':'retrieve'})
delete = DeleteUser.as_view({'delete': 'destroy'})
app_name = 'auth'

urlpatterns = [
    path('algo/', views.login.MyView.as_view()),
    path('algoprotected/',views.login.ProtectedView.as_view()),
    path('login/',login),
    path('register/',register),
    path('delete/<int:pk>/', delete, name='delete_user'),
]