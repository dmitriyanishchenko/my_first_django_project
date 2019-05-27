from django import forms


class CarForm(forms.Form):
    brand = forms.CharField(max_length=255)
    model = forms.CharField(max_length=255)
    color = forms.CharField(max_length=255)
    weight = forms.IntegerField(min_value=700)
    fullname = forms.CharField(max_length=255)
    year = forms.CharField(max_length=255)
