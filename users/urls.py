from django.contrib import admin
from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.register, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('logout/', views.user_logout, name='logout'),
]
