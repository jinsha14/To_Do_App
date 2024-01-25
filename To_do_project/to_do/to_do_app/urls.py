from django.urls import path

from . import views
urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('task', views.task, name='task'),
    path('task_list', views.task_list, name='task_list'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('lg_out', views.lg_out, name='lg_out'),
]