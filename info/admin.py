from django.contrib import admin

from info.models import InfoBlog
from info.models import RentalConsole


# Register your models here.

# admin.site.register(InfoBlog)


@admin.register(InfoBlog)
class InfoBlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'rating', 'price', 'is_deleted',)
    search_fields = ('name', 'rating',)
    list_filter = ('is_deleted',)
    sortable_by = ('rating', 'name', 'id', 'price', 'is_deleted',)


@admin.register(RentalConsole)
class RentalConsoleAdmin(admin.ModelAdmin):
    list_display = ('console', 'game', 'number', 'address', 'delivery_date', 'delivery_time',)
    list_filter = ('console',)
    sortable_by = ('console', 'game', 'number', 'address', 'delivery_date', 'delivery_time',)
