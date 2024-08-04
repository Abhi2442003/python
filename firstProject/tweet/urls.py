from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/', views.tweet_view, name='tweet-view'),
    path('create/', views.tweet_create, name='create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet-edit'),
    path('<int:tweet_id>/delete', views.tweetDelete, name='tweet-delete'),
    path('search/', views.search_view, name='search'),
    path('register/', views.register, name='register'),
]
