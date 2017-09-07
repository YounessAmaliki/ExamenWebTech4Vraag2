from django import forms

class adding(forms.Form):
    nname = forms.CharField(label='Naam', max_length=100)
    nexamen = forms.CharField(label='Calorieen', max_length=100)
    ndatum = forms.CharField(label='Ingredienten', max_length=100)
    nreden = forms.CharField(label='Tijd', max_length=300)
    