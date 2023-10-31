from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from info import views

urlpatterns = [
    path("", views.read_post, name='read_post'),
    path("about/", views.about_rental, name='about_page'),
    path("rules/", views.rental_rules, name='rules_page'),
    path("two/three/", views.rental_rules, name='third_page'),
    path("menu/order/", views.OrderListView.as_view(), name='order-list'),
    path("detail/<int:pk>", views.OrderDetailView.as_view(), name='order-detail'),
    path("order/<int:pk>/update", views.OrderUpdateView.as_view(), name='order-update'),
    path("order/<int:pk>/delete", views.OrderDeleteView.as_view(), name='order-delete'),
    path("order/", views.CreateOrderView.as_view(), name='order-create'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)