from django.db import models
from vendorProfileMngmnt.models import Vendor


# Create your models here.
class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, max_length=20, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(max_length=20)
    quality_rating_avg = models.FloatField(max_length=20)
    average_response_time = models.FloatField(max_length=20)
    fulfillment_rate = models.FloatField(max_length=20)

    def __str__(self):
        return "%s" % self.vendor
