from django.test import TestCase

# Create your tests here.
from weddinglist.models import wedding_list

class wedding_list_test(TestCase):
    def create_item(self):
        wedding_list.objects.create(
            user_list = 2,
            product_id = 1,
            product_name = "Tea pot",
            product_brand = "Le Creuset",
            product_price = 47.00,
            product_qty_ordered = 1,
            product_payment_status = "Pending"
        )
    
    def product_added(self):
        new_item = wedding_list.objects.get(user_list=2)
        self.assertIs(new_item.product_id, "Product name is 'Tea pot'")