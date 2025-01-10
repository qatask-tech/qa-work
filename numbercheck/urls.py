from django.urls import path

from system.views import check_number_view

urlpatterns = [
    path("check/", check_number_view, name="check_number"),
]
