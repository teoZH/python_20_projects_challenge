from django import forms
from recipes_app.models import Recipe
from django.core.exceptions import ValidationError


def validate_positive_integer(data):
    if int(data) < 0:
        raise ValidationError('Please input positive time')
    return data


class SomeInterField(forms.IntegerField):
    default_validators = [validate_positive_integer]

class CreateRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time')
        labels = {
            'title': 'Title',
            'image_url': 'Image URL',
            'description': 'Description',
            'ingredients': 'Ingredients',
            'time': 'Time(Minutes)'
        }
        widgets = {
            'description': forms.Textarea(attrs={
                'cols': '40',
                'rows': '10'
            })
        }

        field_classes = {
            'time': SomeInterField
        }
