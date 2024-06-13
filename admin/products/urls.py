from django.urls import path, include
from .views import (dynamic_look_view, dynamic_look_view_delete, list_of_objects)

urlpatterns = [
    # path("product/", product_detail_view, name="products"),
    # path("product_form/", product_form, name="form"),
    path("/<int:user_id>/", dynamic_look_view, name="product-detail"),
    path("/<int:user_id>/delete", dynamic_look_view_delete, name="delete"),
    path("/", list_of_objects, name="list"),
    # path("contact/", About.contact, name="contact"),
]
