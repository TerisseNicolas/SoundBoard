from django.urls import path

from board import views

urlpatterns = [
    path('', views.index, name='board.index'),
    path('play/<str:name>', views.play, name='board.play'),
    path('play_random/', views.play_random, name='board.play_random'),
    path('upload', views.upload, name='board.upload'),
    path('delete/<str:name>', views.delete, name='board.delete'),
    path('error', views.error, name='board.error')
]
