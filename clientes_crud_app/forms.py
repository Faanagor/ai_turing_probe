from django import forms

class RegForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    categoria=forms.CharField(max_length=50)   