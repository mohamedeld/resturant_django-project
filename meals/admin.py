from meals.models import Category, Meals
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class MealsAdmin(SummernoteModelAdmin,admin.ModelAdmin):  # instead of ModelAdmin
   summernote_fields = '__all__'
   list_display = ['name','preperation_time','people','price']
   search_fields = ['name','description']
   list_filter =('category','people')

admin.site.register(Meals,MealsAdmin)
admin.site.register(Category)