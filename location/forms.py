from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import Branch
from user.models import SalesPerson


class BranchForm(ModelForm):
    branch_head = forms.ModelChoiceField(
        required=False,
        queryset=SalesPerson.persons.managers(),
    )

    class Meta:
        model = Branch
        fields = ['name', 'location', 'branch_head']
