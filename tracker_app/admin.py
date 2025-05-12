from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'amount', 'category', 'date', 'created_at')
    list_filter = ('type', 'category', 'date')
    search_fields = ('title', 'description')
