from django.urls import path

from . import views

urlpatterns = [
    path('', views.match_profiles, name='match_profiles'),
]
