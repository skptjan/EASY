from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexView, name='Home'),
    path('home', views.indexView, name='Home'),
    path('plans', views.plansView, name='Plans'),
    path('contact', views.contactView, name='Contact'),
    path('about-us', views.aboutUsView, name='About-Us'),
    path('login', views.loginView, name="Login"),
    path('register', views.registerView, name="Register"),
    path('logout', views.logoutView, name="Logout"),
    path('dashboard', views.dashboardView, name="Dashboard"),
    path('updateLamp/<str:pk>', views.updateLamp, name="updateLamp"),
    path('deleteLamp/<str:pk>', views.deleteLamp, name="deleteLamp"),
    path('profile', views.profileView, name="Profile"),
    path('404', views.handler404, name="404"),

]