from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    email = forms.EmailField()
    title = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"placeholder": "your title"}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={"class": "new-class-name two",
                                                                              "id": "my-text-id-for-textarea",
                                                                              "row": 20,
                                                                              "cols": 100,
                                                                              "placeholder": "your description"}))
    price = forms.DecimalField(initial=199.9)

    class Meta:
        model = Product
        fields = [
            "title", "description", "price",
        ]

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if "CFC" in title:
    #         return title
    #     else:
    #         raise forms.ValidationError("This in not a valid title")
    #
    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("edu"):
    #         raise forms.ValidationError("This in not a valid email")
    #     else:
    #         return email


class RawProductForm(forms.Form):
    title = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"placeholder": "your title"}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={"class": "new-class-name two",
                                                                              "id": "my-text-id-for-textarea",
                                                                              "row": 20,
                                                                              "cols": 100,
                                                                              "placeholder": "your description"}))
    price = forms.DecimalField(max_digits=3)
