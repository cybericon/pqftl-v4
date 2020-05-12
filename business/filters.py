from django import forms
import django_filters
from .models import Transaction
from user.models import SalesPerson
from location.models import Branch


class TransactionFilter(django_filters.FilterSet):
    transaction_type = django_filters.ChoiceFilter(
        choices=Transaction.type_options, label="Type")
    transaction_status = django_filters.ChoiceFilter(
        choices=Transaction.status_options, label="Status")
    submission_date = django_filters.DateFromToRangeFilter(label="Submission Between", widget=django_filters.widgets.RangeWidget(attrs={
        'type': 'date',
        'class': 'form-control'
    }))
    issuance_date = django_filters.DateFromToRangeFilter(label="Issuance Between", widget=django_filters.widgets.RangeWidget(attrs={
        'type': 'date',
        'class': 'form-control'
    }))

    sales_person__name = django_filters.ModelChoiceFilter(
        queryset=SalesPerson.persons.all(), label="Sales Person")
    sales_person__branch_name__name = django_filters.ModelMultipleChoiceFilter(
        queryset=Branch.locations.all(), label="Branch")

    class Meta:
        model = Transaction
        fields = []
