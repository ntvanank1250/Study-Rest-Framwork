from django.urls import path, include
from .views import (TodoListApiView,TodoDetailAPIView)

urlpatterns =[
    path('', TodoListApiView.as_view()),
    path('<int:todo_id>/', TodoDetailAPIView.as_view()),
]