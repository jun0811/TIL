from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # form Tag
    title = forms.CharField(
        max_length=10,
        label='Title:',
        # 실제로 보여지는 부분(template 담당) - forms 에서 커스터마이징 가능
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder': '제목을 입력해주세요.',
            }
        )
    )
    
    content = forms.CharField(
        label='Content:',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
                'placeholder': '내용을 입력해주세요.',
            }
        )
    )

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title', ) 빼고싶은 것 