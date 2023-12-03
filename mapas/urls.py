from django.urls import path
from mapas.views import ProjectCreate

create = ProjectCreate.as_view({'post':'create'})

urlpatterns = [
    path('create-project/', create, name='create-project'),
]