from django.db import models


def incremental_vendor_id():
    last_vendor = Vendor.objects.all().order_by('vendor_code').last()
    if not last_vendor:
        return "VNDR" + str(0).zfill(6)
    vendor_id = last_vendor.vendor_code
    vendor_int = int(vendor_id[4:10])
    new_vendor_int = vendor_int+1
    new_vendor_id = "VNDR" + str(new_vendor_int).zfill(6)
    return new_vendor_id


# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=20)
    contact_details = models.TextField(max_length=30)
    address = models.TextField(max_length=100)
    vendor_code = models.CharField(primary_key=True,unique=True,default=incremental_vendor_id, max_length=20, editable=False)
    on_time_delivery_rate = models.FloatField(max_length=20, default=0, editable=False)
    quality_rating_avg = models.FloatField(max_length=20, default=0, editable=False)
    average_response_time = models.FloatField(max_length=20, default=0, editable=False)
    fulfillment_rate = models.FloatField(max_length=20, default=0, editable=False)

    def __str__(self):
        return "%s" % self.vendor_code

