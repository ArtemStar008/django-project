from django.contrib import admin

from info.models import InfoBlog


# Register your models here.

# admin.site.register(InfoBlog)


@admin.register(InfoBlog)
class InfoBlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'rating', 'price', 'is_deleted', 'date', 'datetime',)
    search_fields = ('name', 'rating',)
    list_filter = ('is_deleted',)
    sortable_by = ('rating', 'name', 'id', 'price', 'is_deleted', 'date', 'datetime',)

