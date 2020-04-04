from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('thanks/', views.registered, name='thanks'),
    path('signup/', views.create_profile, name='thanks')
]