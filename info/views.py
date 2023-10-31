from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from info.models import RentalConsole
from info.form import OrderForm


# Create your views here.

def read_post(request):
    return render(request, 'db_admin.html')


def about_rental(request):
    return render(request, 'about_rental.html')


def rental_rules(request):
    return render(request, 'rental_rules.html')


class OrderListView(generic.ListView):
    template_name = 'info_blog/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return RentalConsole.objects.filter(is_deleted=False)


class CreateOrderView(generic.CreateView):
    model = RentalConsole
    template_name = 'info_blog/order_create.html'
    # fields = ('text', 'name', 'rating', 'price')
    form_class = OrderForm
    order = OrderForm()

    def get_success_url(self):
        return reverse('order-list')


class CreatePostView(generic.CreateView):
    model = RentalConsole
    templates_name = 'info_blog/order_create.html'
    fields = ('console', 'game', 'number', 'address', 'delivery_date', 'delivery_time', 'is_deleted')


class OrderDetailView(generic.DetailView):
    model = RentalConsole
    template_name = 'info_blog/order_detail.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = RentalConsole.objects.filter(is_deleted=False)
        return context


class OrderUpdateView(generic.UpdateView):
    model = RentalConsole
    template_name = 'info_blog/order_update.html'
    form_class = OrderForm

    def get_success_url(self):
        return reverse('order-list')


class OrderDeleteView(generic.DeleteView):
    model = RentalConsole
    template_name = 'info_blog/order_delete.html'

    def get_success_url(self):
        return reverse('order-list')

    def deleted_true(self):
        if not RentalConsole.is_deleted:
            RentalConsole.objects.filter(is_deleted=True)
