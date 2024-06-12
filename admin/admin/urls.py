"""
URL configuration for admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from new_app.views import About
from products.views import product_detail_view, product_form

urlpatterns = [
    path("", About.home, name="home"),
    path("product/", product_detail_view, name="products"),
    path("product_form/", product_form, name="form"),
    path("contact/", About.contact, name="contact"),
    path("admin/", admin.site.urls),
]