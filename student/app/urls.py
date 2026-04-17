from django.urls import path

# we have to import views module from current folder

from . import views

urlpatterns = [
    path('', views.home), #127.0.0.1:8000/
    path('about', views.about), #127.0.0.1:8000/about
    path('contact', views.contact), #127.0.0.1:8000/contact
    path('discard/<str:roll>', views.discard),
    path('edit/<str:roll>', views.edit),
    path('update/<str:roll>', views.update)
]