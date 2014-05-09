from django import forms

class GridForm(forms.Form):
    grid_number = forms.CharField(max_length=2)

