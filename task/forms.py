from django import forms


class InputForm(forms.Form):
    input_data = forms.CharField(max_length=255)