from django.forms import ModelForm
from django import forms
from cardquest.models import Trainer, Collection, PokemonCard

class TrainerForm(ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Trainer
        fields = "__all__"