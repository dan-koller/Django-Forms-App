from django import forms
from .models import Participants


class RegistrationForm(forms.Form):
    name = forms.CharField(label="your name")
    age = forms.IntegerField(label="your age")
    favorite_book = forms.CharField(label="your favorite book")

    class Meta:
        model = Participants

        fields = [
            "name",
            "age",
            "favorite_book"
        ]
