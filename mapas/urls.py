from django.urls import path, re_path
from .views.createmaps import CreateMaps

createmap = CreateMaps.as_view({'post':'post'})

urlpatterns = [
    path('createmaps/',createmap)
]