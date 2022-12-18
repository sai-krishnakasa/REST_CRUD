from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path('',views.apiOverView,name='api-overview'),
    path('task-list/',views.taskList,name='api-task_list'),
    path('task-detail/<str:pk>',views.taskDetail,name='api-task_detail'),
    path('task-delete/<str:pk>/',views.taskDelete,name='api-task_delete'),
    path('task-create',views.taskCreate,name='api-task_create'),
    path('task-update/<str:pk>',views.taskUpdate,name='api-task_update'),

]