from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Branch
from user.models import SalesPerson
from business.models import Transaction
from .forms import BranchForm
from pqftl.selectors import *

# Create your views here.
# Branch Views Here


class BranchList(LoginRequiredMixin, ListView):
    model = Branch
    context_object_name = 'branches'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'All Branches'
        context['total_managers'] = SalesPerson.persons.managers().count()
        context['total_dsf'] = SalesPerson.persons.dsf().count()
        return context


class BranchDetail(LoginRequiredMixin, DetailView):
    context_object_name = 'branch'
    model = Branch

    def business(self):
        transactions = period_filter(
            self.request, Transaction.records.all().order_by('-submission_date'))
        total, issued, pending, new_cases = branch_business_summary(
            self.object, transactions)
        return {'total_business': total, 'issued_business': issued,
                'pending_business': pending, 'new_cases': new_cases}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.object.name} Branch'
        context.update(self.business())
        context.update({'transactions': period_filter(self.request,
                                                      Transaction.records.filter(Q(sales_person__branch_name=self.object)))})
        return context


class BranchCreate(LoginRequiredMixin, CreateView):
    model = Branch
    form_class = BranchForm
    template_name = 'pqftl/add_update_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Add new Branch'
        return context


class BranchUpdate(LoginRequiredMixin, UpdateView):
    model = Branch
    form_class = BranchForm
    template_name = 'pqftl/add_update_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Update {self.object.name} Branch Details'
        return context


class BranchDelete(LoginRequiredMixin, DeleteView):
    model = Branch
    success_url = reverse_lazy('branch_list')
    template_name = 'pqftl/confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Delete {self.object.name} Branch'
        return context
