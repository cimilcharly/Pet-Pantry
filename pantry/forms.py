from django import forms
from .models import *

class model_form1(forms.ModelForm):
    class Meta:
        model=product
        fields='__all__'

class model_form(forms.ModelForm):
    class Meta:
        model=Register
        fields='__all__'

class model_form2(forms.ModelForm):
    class Meta:
        model=deliveryboy
        fields='__all__'