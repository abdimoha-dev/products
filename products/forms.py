from django import forms
from .models import Product

# class product_form(forms.ModelForm):
#     class Meta:
#         model=Product
#         fields=[
#             'title', 'description', 'price','summary'
#         ]

class product_form(forms.Form):
    title=forms.CharField(required=False,
    widget=forms.TextInput(
        attrs={
            'placeholder': 'enter your title'
        }
    ))
    description=forms.CharField()
    price=forms.DecimalField()
    summary=forms.CharField