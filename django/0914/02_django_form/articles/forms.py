from django import forms

class ArticleForm(forms.Form): # Form Class 상속
    title = forms.CharField(max_length=10)
    content = forms.CharField()