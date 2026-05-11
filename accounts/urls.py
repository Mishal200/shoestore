from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.log_view, name='login'),
]