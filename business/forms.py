from django import forms
from django.forms import ModelForm


from .models import Transaction


class TransactionForm(ModelForm):
    submission_date = forms.CharField(widget=forms.DateInput(attrs={
        'type': 'date'
    }))
    issuance_date = forms.CharField(required=False, widget=forms.DateInput(attrs={
        'type': 'date'
    }))

    def clean_issuance_date(self):
        return None if self.cleaned_data['issuance_date'] == '' else self.cleaned_data['issuance_date']

    class Meta:
        model = Transaction
        fields = '__all__'
