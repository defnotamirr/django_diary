from django.urls import path
from . import views
from .views import DiaryEntryListCreate

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('api/entries/', DiaryEntryListCreate.as_view(), name='entry-list-create'),
]