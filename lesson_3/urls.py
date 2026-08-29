from django.urls import path
from lesson_3 import views

urlpatterns = [
    path('main/', views.main),
    path('main/text/', views.file, name='file'),
]