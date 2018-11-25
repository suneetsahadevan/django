from django import forms

class Get_year_month(forms.Form):
    form_date = forms.DateField(help_text="This is a date field")
