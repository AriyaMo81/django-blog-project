from django import forms


class UserCreateForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    firstname = forms.CharField()
    lastname = forms.CharField()


class UserloginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
