from django.db import models

from vendorProfileMngmnt.models import Vendor


def incremental_product_no():
    last_product = PurchaseOrder.objects.all().order_by('po_number').last()
    if not last_product:
        return "PODR" + str(0).zfill(8)
    product_id = last_product.vendor_code
    product_int = int(product_id[4:12])
    new_product_int = product_int+1
    new_product_id = "VNDR" + str(new_product_int).zfill(8)
    return new_product_id


# Create your models here.
class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=20, editable=False, default=incremental_product_no)
    vendor = models.ForeignKey(Vendor, max_length=20, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    quality_rating = models.FloatField(max_length=20)
    issue_date = models.DateTimeField()
    acknowledgement_date = models.DateTimeField(null=True)

    def __str__(self):
        return "%s" % self.po_number
