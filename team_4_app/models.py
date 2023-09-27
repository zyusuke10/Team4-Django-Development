from django.db import models

class Cart(models.Model):
    product_id = models.CharField('rakuten_product_id', max_length=100, )

    def __str__(self):
        return self.product_id

