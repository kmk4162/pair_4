"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('<int:reivew_pk>/comments/', views.create_comment, name='create_comment'),
    path('<int:reivew_pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
    path('<int:reivew_pk>/', views.detail, name='detail'),
]
