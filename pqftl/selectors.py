import datetime
from django.db.models import Count, Sum, Q
from django.db.models import Value as V
from django.db.models.functions import Coalesce


def period_filter(request, qs):
    if request.method == 'GET' and 'period' in request.GET:
        today = datetime.date.today()
        qtrs = [(x-1)//3+1 for x in range(1, 13)]
        filter_list = [
            ('this_month', {'submission_date__month': today.month}),
            ('last_month', {'submission_date__month': today.month - 1}),
            ('this_qtr', {'submission_date__quarter': qtrs[today.month]}),
            ('last_qtr', {'submission_date__quarter': qtrs[today.month]-1}),
            ('this_year', {'submission_date__year': today.year}),
            ('last_year', {'submission_date__year': today.year - 1}),
        ]
        period = request.GET.get('period', None)

        # period_index = [x[0] for x in filter_list].index(period)
        period_filter = filter_list[[x[0]
                                     for x in filter_list].index(period)][1]
        return qs.filter(**period_filter)
    else:
        return qs


def get_business(qs, filter=None):
    result = qs.aggregate(business=Coalesce(
        Sum('amount', filter=filter), V(0)),
    )
    return result['business']


def business_summary(qs, filter=None):
    total = get_business(qs)
    issued = get_business(qs, filter=Q(transaction_status='Issued'))
    pending = get_business(qs, filter=Q(transaction_status='Pending'))
    new_cases = qs.filter(transaction_type='New').count()
    return {'total_business': total,
            'issued_business': issued,
            'pending_business': pending,
            'new_cases': new_cases, }


def get_branch_business(branch, qs, filter=None):
    if filter == None:
        branch_business = get_business(
            qs.filter(sales_person__branch_name=branch))
    else:
        branch_business = get_business(
            qs.filter(sales_person__branch_name=branch), filter=filter)
    return branch_business


def branch_business_summary(branch, qs):
    total_business = get_branch_business(branch, qs)
    issued_business = get_branch_business(
        branch, qs, filter=Q(transaction_status='Issued'))
    pending_business = get_branch_business(
        branch, qs, filter=Q(transaction_status='Pending'))
    new_cases = qs.filter(sales_person__branch_name=branch).filter(
        transaction_type='New').count()
    return (total_business, issued_business, pending_business, new_cases)


def get_team_business(qs, manager, filter=None):
    business = get_business(
        qs.filter(sales_person__is_manager=False).filter(
            sales_person__reporting_manager=manager), filter=filter
    )
    return business


def get_salesperson_business(qs, salesperson, filter=None):
    business = get_business(
        qs.filter(sales_person=salesperson), filter=filter)
    return business


def get_manager_business(qs, manager, filter=None):
    team_business = get_team_business(qs, manager, filter=filter)
    self_business = get_salesperson_business(qs, manager, filter=filter)
    return team_business + self_business


def salesperson_business_summary(qs, salesperson):
    total_business = 0
    issued_business = 0
    pending_business = 0
    new_cases = 0
    if salesperson.is_manager:
        manager = salesperson
        total_business = get_manager_business(qs, manager)
        issued_business = get_manager_business(
            qs,
            manager,
            filter=Q(transaction_status='Issued'))
        pending_business = get_manager_business(
            qs,
            manager,
            filter=Q(transaction_status='Pending'))
        new_cases = qs.filter(sales_person__is_manager=False).filter(sales_person__reporting_manager=manager).filter(
            transaction_type='New').count()
    else:
        total_business = get_salesperson_business(qs, salesperson)
        issued_business = get_salesperson_business(
            qs,
            salesperson,
            filter=Q(transaction_status='Issued'))
        pending_business = get_salesperson_business(
            qs,
            salesperson,
            filter=Q(transaction_status='Pending'))
        new_cases = qs.filter(sales_person=salesperson).filter(
            transaction_type='New').count()
    return (total_business, issued_business, pending_business, new_cases)
