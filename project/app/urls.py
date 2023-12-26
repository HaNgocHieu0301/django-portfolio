from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('about', views.AboutView.as_view(), name='about'),
    path('project', views.ProjectsView.as_view(), name='projects'),
]
