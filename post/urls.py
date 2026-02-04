from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.posthome, name='posthome'),
    path('newpost/', views.newPost, name='newpost'),
    path('<int:id>/', views.postView, name='postView'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<str:username>/', views.profile, name='profile'),
]

