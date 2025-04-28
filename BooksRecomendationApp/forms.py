from django import forms

class GenreForm(forms.Form):
    genre = forms.CharField(label='Wpisz swój ulubiony gatunek', max_length=100)