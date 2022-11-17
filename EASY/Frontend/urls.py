from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexView, name='Home'),
    path('home', views.indexView, name='Home'),
    path('login', views.loginView, name="Login"),
    path('logout', views.logoutView, name="Logout"),
    path('404', views.handler404, name="404"),

]