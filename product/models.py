from django.db import models

# Create your models here.
PRODUCT_SIZES =(
    ( "XS","Xtra small"),
    ( "S","Small"),
    ( "M", "Medium"),
    ("L","Large"),
    ("XL","Xtra large"),
    
    
)
    
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_fabric_type = models.CharField(max_length=1000)
    colour  = models.CharField(max_length=100)
    sizes   =models.CharField(max_length=2,choices = PRODUCT_SIZES)
    product_description  = models.CharField(max_length=500)

    def __str__(self):
        return self.product_name
