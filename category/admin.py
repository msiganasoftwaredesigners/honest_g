from django.contrib import admin
from category.models import Category, ParkingSpace, Condition, Bedroom, Bathroom, Kitchen
from msigana_ecommerce.admin_site import admin_site
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'category_slug': ('category_name',)}
    list_display = ('category_name', 'category_slug')

    # def has_delete_permission(self, request, obj=None):
    #     return False
    
    # def has_add_permission(self, request, obj=None):
    #     return False


admin_site.register(Category, CategoryAdmin)
admin_site.register(ParkingSpace, admin.ModelAdmin)
admin_site.register(Condition, admin.ModelAdmin)
admin_site.register(Bedroom, admin.ModelAdmin)
admin_site.register(Bathroom, admin.ModelAdmin)
admin_site.register(Kitchen, admin.ModelAdmin)