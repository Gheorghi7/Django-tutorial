from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product

from .forms import ProductForm, RawProductForm


# Create your views here.
def product_detail_view(request):
    # obj = Product.objects.get(id=1)
    obj = get_object_or_404(Product, id=1)
    # try:
    #     obj = Product.objects.get(id=1)
    # except Product.DoesNotExist:
    #     raise Http404

    context = {
        "title": obj.title,
        "description": obj.description
    }
    return render(request, "products/product_detail.html", context)


# def product_form(request):
#     initial_forms = {
#         "title": "my awesome title",
#     }
#     form = ProductForm()
#     if request.method == "POST":
#         form = ProductForm(request.POST or None, initial=initial_forms)
#
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     context = {
#          "form": form
#     }
#     return render(request, "products/product_create.html", context)
#
def product_form(request):
    initial_forms = {
        "title": "my awesome title",
        "email": "my email"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    # if request.method == "POST":
    #     form = ProductForm(request.POST or None, initial=initial_forms)
    #
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         Product.objects.create(**form.cleaned_data)
    #     else:
    #         print(form.errors)
    context = {
        "form": form
    }
    return render(request, "products/product_create.html", context)


def dynamic_look_view(request, user_id):
    # obj = Product.objects.get(id=user_id)
    # query = Product.objects.all() # list of a objects
    obj = get_object_or_404(Product, id=user_id)
    context = {

        "objects": obj
    }
    return render(request, "products/dynamic.html", context)


def dynamic_look_view_delete(request, user_id):
    obj = get_object_or_404(Product, id=user_id)
    if request.method == "POST":
        obj.delete()
    context = {
        "objects": obj
    }

    return render(request, "products/product_delete.html", context)


def list_of_objects(request):
    quaery = Product.objects.all()
    context = {
        "objects": quaery
    }
    return render(request, "products/product_list.html", context)


