from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.AboutView.as_view(), name='about'),
    path('project', views.project, name='projects'),
]
