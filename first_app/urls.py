from django.template.defaulttags import url
from first_app import views
from django.urls import path
from django.contrib import admin

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),

]


