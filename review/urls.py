from django.urls import path
from . import views
urlpatterns = [
    path('', views.reviews, name='reviews'),
    path("like/", views.like_review, name="like_review"),
    path('add/', views.add_review, name='add_review'),
]