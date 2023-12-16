from django.urls import path
from .views import PurchasOrderList, PurchaseOrderDetail

urlpatterns = [
    path('', PurchasOrderList.as_view()),
    path('<str:pk>/', PurchaseOrderDetail.as_view()),
]
