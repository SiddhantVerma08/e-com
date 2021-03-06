from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Shophome"),
    path("about", views.about, name="AboutUs"),
    path("contact", views.contact, name="ContactUs"),
    path("tracker", views.tracker, name="Tracking"),
    path("search", views.search, name="Search"),
    path("productview", views.productview, name="Product"),
    path("checkout", views.checkout, name="Checkout"),
]
