from django.db import models


# Create your models here.
class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(max_length=20)
    date = models.TextField(max_length=30)
    on_time_delivery_rate = models.FloatField(max_length=20)
    quality_rating_avg = models.FloatField(max_length=20)
    average_response_time = models.FloatField(max_length=20)
    fulfillment_rate = models.FloatField(max_length=20)

    def __str__(self):
        return "%s" % self.name