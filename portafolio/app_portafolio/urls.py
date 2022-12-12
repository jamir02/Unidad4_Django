from . import views
from django.urls import path

app_name= 'app_portafolio'

urlpatterns =[
    path("", views.index,name="index"),
    path("portafolio_usuario",views.portafolio_usuario,name= "portafolio_usuario"),
    path("create_new_user",views.create_new_user,name= "create_new_user"),
]
