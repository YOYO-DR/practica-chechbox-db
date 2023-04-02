from django.urls import path
from .views import *

urlpatterns = [
  path('actu/<int:id>/',actualizar_valor,name='actualizar_valor'),
  path('',vista,name='vista'),
]
