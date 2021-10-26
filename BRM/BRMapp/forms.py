from django import forms

class NewBookForm(forms.Form):
    title=forms.CharField(label='Title',max_length=100)
    author=forms.CharField(label='Author')
    price=forms.IntegerField(label='Price')
    publisher=forms.CharField(label='Publisher')

class SearchForm(forms.Form):
    title=forms.CharField(label='Title',max_length=100)    