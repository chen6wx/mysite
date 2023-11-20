from django.contrib import admin
from .models import Item, Receipt
# Register your models here.


class ItemInLineAdmin(admin.TabularInline):
    model = Item


class ReceiptAdmin(admin.ModelAdmin):
    inlines = [ItemInLineAdmin]


admin.site.register(Receipt, ReceiptAdmin)


admin.site.register(Item)