"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as v
from .views import PostCommentView

# from mysite.views import LoginView
#admin.site.register(Post)
urlpatterns = [
    path('', views.home, name= 'home'),
    path("post-comment/", PostCommentView.as_view()),
    path('admin/', admin.site.urls), 
    path("about/", views.about, name="about"),
    path("games/", views.games, name="games"),
    path('', views.rus, name="rus"),
    path("login/", views.user_login, name="login"),
    path("registration/", views.register, name="registration"),
    path('logout/', views.logout_view, name="logout"),
    # path('accounts/logout/',v.LogoutView.as_view(next_page='/'),name="logout")
  
    # path('/', include('django.contrib.auth.urls')),
  
]

