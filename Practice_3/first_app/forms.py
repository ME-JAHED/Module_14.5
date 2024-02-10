from django import forms
from django.forms.widgets import NumberInput
from .models import ExampleModels

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]


class ExampleForm(forms.Form):
    name = forms.CharField(initial='Your name')
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), required = False)
    email = forms.EmailField(label="Please enter your email address")
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    favorite_color1 = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color2 = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors3 = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors4 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES)


class Example(forms.ModelForm):
    class Meta:
        model=ExampleModels
        fields= '__all__'
