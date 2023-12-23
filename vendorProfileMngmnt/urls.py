from django.urls import path, include
from .views import VendorList, VendorDetail

urlpatterns = [
    path('', VendorList.as_view()),
    path('<str:pk>/', VendorDetail.as_view()),
    path('', include("performance_metrics.urls")),
]
