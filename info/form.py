from django import forms

from info.models import RentalConsole


# class InfoBlogForm(forms.ModelForm):
#     class Meta:
#         model = InfoBlog
#         fields = ('text', 'name', 'rating', 'price')


class OrderForm(forms.ModelForm):
    class Meta:
        model = RentalConsole
        fields = ('console', 'game', 'number', 'address', 'delivery_date', 'delivery_time')