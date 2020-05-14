from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from pqftl.selectors import *
from user.models import SalesPerson
from location.models import Branch
from business.models import Transaction


@login_required(login_url='login')
def dashboard(request):
    transactions = period_filter(request, Transaction.records.all())
    branches = Branch.locations.all().order_by('id')
    all_managers = SalesPerson.persons.managers()
    all_dsf = SalesPerson.persons.dsf()

    # Setting Chart Data
    y_values = [get_branch_business(
        branch, transactions) for branch in branches]
    x_values = [branch.name for branch in branches]

    zero_branches_indices = [x for x in range(
        0, len(y_values)) if y_values[x] == 0]
    zero_branches = [x_values[x] for x in zero_branches_indices]

    # setting Managers Businesses
    managers = [(manager, manager.branch_name, get_manager_business(
        transactions, manager)) for manager in all_managers]

    managers.sort(key=lambda x: x[2])
    managers.reverse()
    managers_list = [{'manager': manager[0], 'branch': manager[1],
                      'business': manager[2]} for manager in managers]

    # setting dsf Businesses
    dsf = [(dsf, dsf.branch_name, get_salesperson_business(
        transactions, dsf)) for dsf in all_dsf]

    dsf.sort(key=lambda x: x[2])
    dsf.reverse()
    dsf_list = [{'dsf': dsf[0], 'branch': dsf[1],
                 'business': dsf[2]} for dsf in dsf]

    context = {
        'title': 'Dashboard',
        'top_managers': managers_list[:3],
        'top_consultants': dsf_list[:3],
        'zero_managers': [x[0] for x in managers if x[2] == 0],
        'zero_branches': zero_branches,
        'branches': x_values,
        'business': y_values,
    }
    context.update(business_summary(transactions))
    return render(request, 'pqftl/dashboard_main.html', context)


@login_required(login_url='login')
def logout_page(request):
    logout(request)
    messages.success(
        request, f'You are logged out successfully'
    )
    if request.META.get('HTTP_REFERER'):
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('home')
