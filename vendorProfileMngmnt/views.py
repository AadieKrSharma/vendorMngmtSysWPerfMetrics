from rest_framework import generics

from .models import Vendor
from .serializers import VendorSerializer


class VendorList(generics.ListCreateAPIView):
    serializer_class = VendorSerializer

    def get_queryset(self):
        queryset = Vendor.objects.all()
        vendor = self.request.query_params.get('vendor_id')
        if vendor is not None:
            queryset = queryset.filter(vendor_id=vendor)
        return queryset


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()
