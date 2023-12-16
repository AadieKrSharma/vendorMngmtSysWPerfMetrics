from django.urls import path, include
from api import views

urlpatterns = [
    path('vendors/', include('vendorProfileMngmnt.urls')),
    path('purchase_orders/', include('purchaseOrdrMngmnt.urls'))
]
