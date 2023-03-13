from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.



# CarModelInline class
class CarModelInLine(admin.StackedInline):
    model = CarModel
    extra = 5

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('model_make','model_name', 'model_year')
    list_filter = ['model_make']
    search_fields = ['name', 'description']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInLine]
    list_display = ('model_make','model_name', 'model_year')
    list_filter = ['model_make']
    search_fields = ['name', 'description']

# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)