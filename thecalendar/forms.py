from django import forms
from .MonthYearWidget import MonthYearWidget


class Get_year_month(forms.Form):
    year_month = forms.DateField(required=False, widget=MonthYearWidget(years=range(2017,2021)))
    def __str__(self):
        return self.year_month
