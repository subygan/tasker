from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('thanks/', views.registered, name='thanks'),
    path('signup/', views.sign_up, name='thanks'),
    path('sign_in/', views.sign_in, name='signin'),
    path('profile/', views.profile, name='profile'),
]