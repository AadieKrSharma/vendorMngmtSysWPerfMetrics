from django.urls import path, include
from .views import HistoricalPerformanceDetail

urlpatterns = [
    path('<str:pk>/performance', HistoricalPerformanceDetail.as_view()),
]
