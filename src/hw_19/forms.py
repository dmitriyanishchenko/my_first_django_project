from django import forms


class PostForm(forms.Form):
    name = forms.CharField(max_length=20)
    city_from = forms.CharField(max_length=20)
    city_to = forms.CharField(max_length=20)
    number = forms.IntegerField(min_value=0, max_value=50)
    date = forms.CharField(max_length=20)
