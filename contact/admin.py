from django.contrib import admin
from contact import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('-id',)

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone' , 'show')
    ordering = ('-id',)
    search_fields = ('first_name', 'last_name', 'email')
    list_editable = ('show',)
    list_per_page = 10
    list_max_show_all = 200