from rest_framework import generics

from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer


class PurchasOrderList(generics.ListCreateAPIView):
    serializer_class = PurchaseOrderSerializer

    def get_queryset(self):
        queryset = PurchaseOrder.objects.all()
        po_number = self.request.query_params.get('po_number')
        if po_number is not None:
            queryset = queryset.filter(po_number=po_number)
        return queryset


class PurchaseOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PurchaseOrderSerializer
    queryset = PurchaseOrder.objects.all()
