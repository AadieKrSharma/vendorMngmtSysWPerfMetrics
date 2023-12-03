from django.db import models


# Create your models here.
class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=20)
    vendor = models.TextField(max_length=30)
    order_date = models.TextField(max_length=100)
    delivery_date = models.CharField(max_length=10)
    items = models.JSONField
    quantity = models.FloatField(max_length=20)
    status = models.FloatField(max_length=20)
    quality_rating = models.FloatField(max_length=20)
    issue_date = models.DateTimeField
    acknowledgement_date = models.DateTimeField

    def __str__(self):
        return "%s" % self.po_number
