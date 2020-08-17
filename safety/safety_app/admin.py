from django.contrib import admin
from .models import Brand,Category,Item

# Register your models here.
admin.site.site_header = "Safety Admin"
admin.site.site_title = "Safety Admin Portal"
admin.site.index_title = "Welcome to Safety Product Portal"


class ItemAdmin(admin.ModelAdmin):
    list_display = ("title","price","discount","brand_name","category_name","colour","size","weight","discription","modify_date","expiry_date","create_date")
    empty_value_display = 'Unknown Item field'

admin.site.register(Item,ItemAdmin)
admin.site.register(Brand)
admin.site.register(Category)






