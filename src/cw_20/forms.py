from django import forms


class CustomerForm(forms.Form):
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    age = forms.IntegerField()
    profession = forms.CharField(max_length=255)
