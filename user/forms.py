from django import forms
from django.forms import ModelForm

from .models import SalesPerson, Designation
from location.models import Branch


class SalesPersonForm(ModelForm):
    branch_name = forms.ModelChoiceField(
        required=False,
        queryset=Branch.locations.all(),
    )

    reporting_manager = forms.ModelChoiceField(
        required=False,
        queryset=SalesPerson.persons.managers(),
    )

    designation = forms.ModelChoiceField(
        required=False,
        queryset=Designation.titles.all(),
    )

    class Meta:
        model = SalesPerson
        fields = ['name', 'branch_name', 'designation',
                  'is_manager', 'reporting_manager']


class DesignationForm(ModelForm):
    class Meta:
        model = Designation
        fields = ['name']
