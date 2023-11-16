from django.contrib import admin
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    readonly_fields = ('category',)

admin.site.register(Cart, CartAdmin)