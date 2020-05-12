from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Transaction
from user.models import SalesPerson, Designation
from location.models import Branch
from pqftl.selectors import *
from .forms import TransactionForm
from .filters import TransactionFilter


# Create your views here.

# Create your views here.


@login_required(login_url='login')
def transaction_list(request):
    f = TransactionFilter(request.GET, queryset=Transaction.records.all())
    qs = f.qs
    branches = Branch.locations.all()
    all_dsf = SalesPerson.persons.dsf()

    # Branch monthly business
    branch_wise_business_monthly_business = []
    # today = datetime.date.today()

    for branch in branches:
        branch_business = []
        for i in range(1, 13):
            # if i > today.month:
            #     break
            branch_business.append(get_branch_business(
                branch, qs, filter=Q(submission_date__month=i)))
        branch_wise_business_monthly_business.append(
            {'branch': branch.name, 'business': branch_business})

    # Branch Contribution Share
    y_values = [get_branch_business(
        branch, qs) for branch in branches]
    x_values = [branch.name for branch in branches]

    # Top Performers
    dsf = [(dsf.name, dsf.branch_name, get_salesperson_business(
        qs, dsf)) for dsf in all_dsf]

    dsf.sort(key=lambda x: x[2])
    dsf.reverse()
    dsf_list = [[dsf[0], dsf[2]] for dsf in dsf]
    dsf_names = [dsf[0] for dsf in dsf_list]
    dsf_business = [dsf[1] for dsf in dsf_list]

    context = {
        'form': f.form,
        'title': 'All Business Transactions',
        'transactions': qs,
        'branches': x_values,
        'business': y_values,
        'top_consultants': dsf_names[:5],
        'top_consultants_business': dsf_business[:5],
        'business_trend_data': branch_wise_business_monthly_business,
    }
    context.update(business_summary(qs))

    return render(request, 'business/transaction_list.html', context)


class TransactionDetail(LoginRequiredMixin, DetailView):
    context_object_name = 'transaction'
    model = Transaction

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.object}'
        return context


class TransactionCreate(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'pqftl/add_update_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Add new Business'
        return context


class TransactionUpdate(LoginRequiredMixin, UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'pqftl/add_update_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Update {self.object} Transaction'
        return context


class TransactionDelete(LoginRequiredMixin, DeleteView):
    model = Transaction
    success_url = reverse_lazy('transaction_list')
    template_name = 'pqftl/confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Delete {self.object}'
        return context
