from django.contrib import admin
from .models import Contact, Product

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')
    list_filter = ('email',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Product, ProductAdmin)