from django import forms


class TodoCreateForm(forms.Form):
    title = forms.CharField(label="titles")
    body = forms.CharField()
    created = forms.DateTimeField()
