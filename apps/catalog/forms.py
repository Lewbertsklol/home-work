from django import forms
from .models import Product, Censor


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def clean_name(self):
        name = self.cleaned_data['name'].lower()
        for censured_word in Censor.objects.values_list('word', flat=True):
            if censured_word.lower() in name:
                raise forms.ValidationError('Название не прошло цензуру')
        return name

    def clean_description(self):
        description = self.cleaned_data['description'].lower()
        for censured_word in Censor.objects.values_list('word', flat=True):
            if censured_word.lower() in description:
                raise forms.ValidationError('Описание не прошло цензуру')
        return description
