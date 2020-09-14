from django import forms
from .models import Article

class ArticleForm(forms.Form):
    class Meta:
        model = Article
        fields = '__all__' # 하나만 보여주고싶으면 field = ('title',)
        # exclude = ('title',) 둘 중에 하나만 쓸것...
        

    