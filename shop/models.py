from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    catergory = models.CharField(max_length=50 , default ="")
    desc = models.CharField(max_length=200)
    price = models.IntegerField(default =0)
    image = models.ImageField(upload_to="shop/images", height_field=None, width_field=None, max_length=None , default ="")

    def __str__(self):
        return self.product_name