from django.urls import path, include
from google.views import HelloView

urlpatterns = [
    path('hello/',HelloView.as_view(), name='hello'),
]