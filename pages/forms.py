from django import forms

class SquareForm(forms.Form):
    number = forms.IntegerField()