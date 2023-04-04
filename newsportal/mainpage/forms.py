from django.forms import ModelForm, TextInput, Textarea
from .models import Supply_news

class SupplyNewsForm(ModelForm):
    class Meta:
        model = Supply_news
        fields = ['supply_title', 'supply_post', 'supply_author']

        widgets = {
            'supply_title': TextInput(attrs={
                'class': 'input_field',
                'placeholder': 'Название статьи'
            }),
            'supply_post': Textarea(attrs={
                'class': 'input_field_textarea',
                'placeholder': 'Текст статьи'
            }),
            'supply_author': TextInput(attrs={
                'class': 'input_field',
                'placeholder': 'Автор'
            }),
        }
