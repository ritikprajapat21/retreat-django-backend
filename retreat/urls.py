from django.urls import path

from . import views

urlpatterns = [
    path('seed', views.seed),
    path('retreats', views.fetchRetreats),
    path('book', views.book)
]