from django import forms

class Get_year_month(forms.Form):
    date = forms.DateField(
    required=False, widget=MonthYearWidget(years=xrange(2017,2010))
    )
