from django.urls import path
from .views import ReportPageView

urlpatterns = [
    path("", ReportPageView.as_view(), name="report"),
]