from django.db import models

# Create your models here.
class wedding_list(models.Model):
    user_list = models.IntegerField()
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=200)
    product_brand = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_qty_ordered = models.FloatField()
    product_payment_status = models.CharField(max_length=50,default="Pending")
    date_added = models.DateTimeField(auto_now_add=True)