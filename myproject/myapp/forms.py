from django import forms

SHIFT = (
    ("1","Morning"),
    ("2","Afternoon"),
    ("3","Evening"),
)

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    shift = forms.ChoiceField(choices=SHIFT)
    time_log = forms.TimeField(help_text="Enter the exact text")
