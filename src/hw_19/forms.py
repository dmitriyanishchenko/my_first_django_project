from django import forms


class PostForm(forms.Form):
   name = forms.CharField(max_length=20)
   lastname = forms.CharField(max_length=20)
   age = forms.IntegerField(min_value=0, max_value=50)
   comment = forms.CharField(max_length=300, widget=forms.Textarea)

