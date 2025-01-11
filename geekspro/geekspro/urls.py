from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/tasks/', views.get_tasks, name='task_list'),
    path('api/v1/tasks/<int:id>/', views.tasks_detail_api_view, name='task_detail'),
]
