from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a Excel file')


class CheckboxForm(forms.Form):
    checkbox = forms.BooleanField()