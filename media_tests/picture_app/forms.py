from .models import Cars
from django import forms


class CarsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['model'].widget.attrs.update({'id': 'model', 'name': 'model', 'class': 'form-control'})
        self.fields['age'].widget.attrs.update({'id': 'age', 'name': 'age', 'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'id': 'price', 'name': 'price', 'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'id': "image", 'name': 'image', 'class': 'form-control'})
