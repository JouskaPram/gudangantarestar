from django.contrib import admin
from scanantares.models import *

class SortirAdmin(admin.ModelAdmin):
    list_display = ['barcode', 'scanner', 'created_at',]
    search_fields = ['barcode', 'scanner', 'created_at',]
    list_filter = ('scanner',)
    list_per_page = 10

class ScannerAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Sortir, SortirAdmin)
# admin.site.register(Scanner, ScannerAdmin)

admin.site.site_header = 'Antarestar'
admin.site.site_title = "Gudang Antares"
admin.site.index_title = "Antarestar Admin"