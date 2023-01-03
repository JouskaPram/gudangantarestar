from django.contrib import admin
from scanantares.models import *

class SortirAdmin(admin.ModelAdmin):
    list_display = ['barcode', 'scanner_id', 'created_at',]
    search_fields = ['barcode', 'scanner_id', 'created_at',]
    list_filter = ('scanner_id',)
    list_per_page = 10

class ScannerAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Sortir, SortirAdmin)
admin.site.register(Scanner, ScannerAdmin)