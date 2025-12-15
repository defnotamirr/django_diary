from django.urls import path
from . import views

urlpatterns = [
    path('zamanbank/', views.zamanmain, name='main'),
]