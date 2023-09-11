from django.urls import path, re_path
#from rest_framework.urlpatterns import format_suffix_format
from firebaseauth import views
from .views.login import MyViewSet

user = MyViewSet.as_view({'post': 'create'})
message = MyViewSet.as_view({'get':'getTest'})
app_name = 'auth'

urlpatterns = [
    path('algo/', views.login.MyView.as_view()),
    path('algoprotected/',views.login.ProtectedView.as_view()),
    path('create/',user),
    path('mensaje/',message),
]