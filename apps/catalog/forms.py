from django import forms
from .models import Product, Censor


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price', 'is_published']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_published'].widget.attrs['hidden'] = True
        self.fields['is_published'].label = ''

    def clean_name(self):
        name = self.cleaned_data['name'].lower()
        stop_words = []
        for censured_word in Censor.objects.values_list('word', flat=True):
            if censured_word.lower() in name:
                stop_words.append(censured_word)
        if stop_words:
            raise forms.ValidationError(f'Содержутся запрещенные слова: {', '.join(stop_words)}')
        return name

    def clean_description(self):
        description = self.cleaned_data['description'].lower()
        stop_words = []
        for censured_word in Censor.objects.values_list('word', flat=True):
            if censured_word.lower() in description:
                stop_words.append(censured_word)
        if stop_words:
            raise forms.ValidationError(f'Содержутся запрещенные слова: {', '.join(stop_words)}')
        return description


class ModeratorProductForm(ProductForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].disabled = True
        self.fields['image'].disabled = True
        self.fields['price'].disabled = True
        self.fields['is_published'].widget.attrs['hidden'] = False
        self.fields['is_published'].label = 'Опубликован:'
