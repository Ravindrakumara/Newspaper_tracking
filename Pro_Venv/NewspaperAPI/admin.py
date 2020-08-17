from django.contrib import admin
from.models import Consumer, Newspaper, Intake, Consumer_order, Daily_Cart #', Order,  Regi,,Newspaper_Payment'
# Register your models here.

admin.site.site_header = "PaperMan Admin"
admin.site.site_title = "PaperMan Admin Portal"
admin.site.index_title = "Welcome to PaperMan Portal"


class ConsumerAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'telephone','email']
    list_editable = [ 'address', 'telephone','email']
    empty_value_display = 'Unknown Item field'
    list_per_page = 1

class NewspaperAdmin(admin.ModelAdmin):
    list_display = ("newspaper", "language", "wh_price", "sa_price","description","company","publication")
    search_fields = ['newspaper', 'publication']
    empty_value_display = 'Unknown Item field'


admin.site.register(Newspaper,NewspaperAdmin)
admin.site.register(Consumer,ConsumerAdmin)
admin.site.register(Consumer_order)
admin.site.register(Intake)
"""admin.site.register(Regi)"""
admin.site.register(Daily_Cart)
"""admin.site.register(Newspaper_Payment)"""
