from django.db import models
from django.urls import reverse
from user.models import SalesPerson
from django.db.models import QuerySet


class TransactionQuerySet(QuerySet):
    def new(self):
        return self.filter(transaction_type='New')

    def modal(self):
        return self.filter(transaction_type='Modal')


class Transaction(models.Model):
    type_options = (
        ('New', 'New'),
        ('Modal', 'Modal')
    )
    status_options = (
        ('Issued', 'Issued'),
        ('Pending', 'Pending'),
        ('In Process', 'In Process')
    )
    transaction_type = models.CharField(max_length=30, choices=type_options)
    transaction_status = models.CharField(
        max_length=30, choices=status_options)
    submission_date = models.DateField()
    issuance_date = models.DateField(null=True, blank=True)
    amount = models.IntegerField()
    sales_person = models.ForeignKey(
        SalesPerson, on_delete=models.SET_DEFAULT, default=4, related_name='business')

    records = TransactionQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse("transaction_list")

    def __str__(self):
        return f" {self.sales_person.name} - {self.sales_person.branch_name.name} - {self.amount}"
