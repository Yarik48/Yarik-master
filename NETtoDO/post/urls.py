"""NETtoDO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_page,name='home_page'),
    path('day/<int:day_id>/', views.show_day, name='day'),
    path('add_post', views.add_post, name='add_post'),
    path('<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('<int:pk>/edit/', views.post_edit, name='edit_post'),

]


