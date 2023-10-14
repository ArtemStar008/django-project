from django.urls import path
from info import views

urlpatterns = [
    path("", views.read_post, name='read_post'),
    path("two/", views.second_page, name='second_page'),
    path("three/", views.third_page, name='third_page'),
    path("two/three/", views.third_page, name='third_page'),

]