from django.urls import path
from info import views

urlpatterns = [
    path("", views.read_post, name='read_post'),
    path("two/", views.second_page, name='second_page'),
    path("three/", views.third_page, name='third_page'),
    path("two/three/", views.third_page, name='third_page'),
    # path("test/", views.MyView.as_view(), name='test'),
    path("posts/", views.PostsView.as_view(), name='posts'),
    path("posts/<int:id>", views.PostsView.as_view(), name='post'),

]