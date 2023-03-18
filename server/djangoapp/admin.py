from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.

# CarModelInline class
class CarModelInLine(admin.StackedInline):
    model = CarModel
    extra = 5

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('model_make','model_name', 'model_dealer')
    list_filter = ['model_make', 'model_dealer']
    search_fields = ['model_name', 'model_year']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInLine]
    list_display = ('make_name','make_description')
    search_fields = ['model_name']

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)