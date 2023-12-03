from django.db import models


# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=20)
    contact_details = models.TextField(max_length=30)
    address = models.TextField(max_length=100)
    vendor_code = models.CharField(max_length=20)
    on_time_delivery_rate = models.FloatField(max_length=20)
    quality_rating_avg = models.FloatField(max_length=20)
    average_response_time = models.FloatField(max_length=20)
    fulfillment_rate = models.FloatField(max_length=20)

    def __str__(self):
        return "%s" % self.vendor_code
