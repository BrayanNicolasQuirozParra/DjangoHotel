
from django.urls import path
from . import views

app_name = "inicio"

urlpatterns = [
    path("inicio", views.list, name="list_inicio"),
    path('habitacionescrear', views.habitaciones, name="crear_habitaciones"),
    path('turismocrear', views.turismo, name="crear_turismoo"),
    path('mirarturismo', views.list_turismo, name="list_turismo"),
]