from django.urls import path
from . import views

urlpatterns = [
    path('', views.recommend_books, name='recommend_books'),
]