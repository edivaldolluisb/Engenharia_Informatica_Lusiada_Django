from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ano/', views.anos, name='anos'),
    path('ano/<int:disciplina_id>', views.ver_disciplina, name='ver_disciplina'),
    path('calendario/', views.calendario, name='calendario'),
    path('agenda/', views.agenda, name='agenda'),
]