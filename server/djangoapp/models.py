from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
# User model
class CarMake(models.Model):
    make_name = models.CharField(null=False, max_length=30, default='Audi')
    make_description = models.CharField(null=False, max_length=30, default='description')
    
    # Create a toString method for object string representation
    def __str__(self):
        return self.make_name + " - " + self.make_description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'vagon'
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'WAGON')
    ]
    model_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    model_dealer = models.IntegerField(null=False)
    model_name = models.CharField(null=False, max_length=30, default='Audi')
    model_type = models.CharField(max_length=30, choices=CAR_TYPES, default=SEDAN)
    model_year = models.DateField(null=False, max_length=30)
    
    # Create a toString method for object string representation
    def __str__(self):
        return self.model_name + " " + " (" + self.model_type + ")"


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
