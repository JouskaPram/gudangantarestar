from django.contrib import admin
from scanantares.models import Sortir, Scanner

class SortirAdmin(admin.ModelAdmin):
    list_display = ['barcode', 'jumlah', 'tanggal', 'scanner_id']
    search_fields = ['barcode', 'jumlah', 'tanggal']
    list_filter = ('scanner_id',)
    list_per_page = 10


admin.site.register(Sortir, SortirAdmin)
admin.site.register(Scanner)