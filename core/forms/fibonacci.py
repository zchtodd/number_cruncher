from django import forms


class FibonacciForm(forms.Form):
    number = forms.IntegerField(label="Enter a number", min_value=0)
