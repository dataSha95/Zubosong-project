from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('programs/', views.programs, name='programs'),
    path('community/', views.community, name='community'),
    path('get-involved/', views.get_involved, name='get_involved'),
    path('contact/', views.contact, name='contact'),
]
