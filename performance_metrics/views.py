from rest_framework import generics

from .models import HistoricalPerformance
from .serializers import HistoricalPerformanceSerializer


class HistoricalPerformanceCalculator(generics.ListCreateAPIView):
    serializer_class = HistoricalPerformanceSerializer

    def get_queryset(self):
        queryset = HistoricalPerformance.objects.all()
        vendor = self.request.query_params.get('vendor_code')
        if vendor_code is not None:
            queryset = queryset.filter(vendor=vendor)
        return queryset


class HistoricalPerformanceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HistoricalPerformanceSerializer
    queryset = HistoricalPerformance.objects.all()
