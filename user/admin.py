from django.contrib import admin
from .models import Designation, Profile, SalesPerson
from business.models import Transaction

# Register your models here.


def make_consultant(modeladmin, request, queryset):
    queryset.update(designation=5)


def make_unithead(modeladmin, request, queryset):
    queryset.update(designation=4)


make_consultant.short_description = "Mark selected persons as consultant"
make_unithead.short_description = "Mark selected persons as Unit Head"


class TransactionInline(admin.TabularInline):
    model = Transaction


class SalesPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch_name', 'designation', 'reporting_manager')
    list_per_page = 20
    list_editable = ('branch_name', 'designation', 'reporting_manager')
    actions = [make_consultant, make_unithead]
    list_filter = ('branch_name', 'is_manager', 'designation')
    inlines = [TransactionInline]


admin.site.register(Designation)
admin.site.register(SalesPerson, SalesPersonAdmin)
admin.site.register(Profile)
