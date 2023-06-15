from django.contrib import admin
from .models import *

from .forms import *
# Register your models here.


class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'picture_of_content', 'is_published','category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'id','category')
    list_editable = ('is_published',)
    list_filter = ('id', 'title', 'time_create', 'time_update', 'is_published')
    prepopulated_fields = {'slug':('title',)}





class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'picture_of_Category')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name', 'id')
    prepopulated_fields = {'slug':('name',)}



admin.site.register(Content, ContentAdmin)
#admin.site.register(Person)
admin.site.register(Category, CategoryAdmin)


