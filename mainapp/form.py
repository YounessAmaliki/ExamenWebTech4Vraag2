from django import forms

class adding(forms.Form):
    nname = forms.CharField(label='Naam', max_length=100)
    ncalorieen = forms.CharField(label='Calorieen', max_length=100)
    ningredienten = forms.CharField(label='Ingredienten', max_length=100)
    ntijd = forms.CharField(label='Tijd', max_length=300)
    