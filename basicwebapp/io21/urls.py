from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('our-works/', views.ourwork, name='our-works'),
    path('press-releases/', views.pressreleases, name='press-releases'),
    path('contact/', views.contact, name='contact'),
]