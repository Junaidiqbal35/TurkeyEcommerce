# Register your models here.
from django.contrib import admin
from .models import Category
from .models import SubCategory
# Register your models here.
#----------------------------------------------------------------
class CategoryAdmin(admin.ModelAdmin):
   #pre populate field 
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')
#---------------------------------------------------------------

class SubCategoryAdmin(admin.ModelAdmin):
   #pre populate field 
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title','main_category', 'slug')
# pass the class to register function 
admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)

#-----------------------------------------------------------------