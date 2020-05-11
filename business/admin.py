from django.contrib import admin
from.models import Transaction

# Register your models here.


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('sales_person', 'branch', 'amount',
                    'transaction_type', 'transaction_status', 'submission_date', 'issuance_date')
    list_per_page = 15
    list_editable = ('amount', 'transaction_type',
                     'transaction_status', 'issuance_date')
    list_filter = ('sales_person__branch_name',
                   'transaction_type', 'transaction_status')

    def branch(self, obj):
        return obj.sales_person.branch_name.name


admin.site.register(Transaction, TransactionAdmin)
