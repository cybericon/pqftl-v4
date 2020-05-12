from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

from .models import SalesPerson, Designation
from business.models import Transaction
from pqftl.selectors import *
from .forms import SalesPersonForm, DesignationForm

# Create your views here.


class SalesPersonList(LoginRequiredMixin, ListView):
    queryset = SalesPerson.persons.managers()
    context_object_name = 'managers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'All Managers'
        return context


class SalesPersonDetail(LoginRequiredMixin, DetailView):
    context_object_name = 'salesperson'
    model = SalesPerson

    def business(self):
        transactions = period_filter(
            self.request, Transaction.records.all().order_by('-submission_date'))
        total, issued, pending, new_cases = salesperson_business_summary(
            transactions,
            self.object)
        return {'total_business': total, 'issued_business': issued,
                'pending_business': pending, 'new_cases': new_cases}

    def get_transactions(self):
        transactions = period_filter(
            self.request, Transaction.records.all().order_by('-submission_date'))
        return transactions.filter(
            Q(sales_person=self.object) | (Q(sales_person__is_manager=False)
                                           & Q(sales_person__reporting_manager=self.object))
        )

    def dsf_business(self):
        if self.object.is_manager:
            transactions = period_filter(
                self.request, Transaction.records.all().order_by('-submission_date'))
            dsf_business = []
            managers_business = []
            for member in self.object.get_dsf():
                total, issued, pending, new_cases = salesperson_business_summary(
                    transactions,
                    member)
                dsf_business.append({
                    'name': member,
                    'total_business': total,
                    'issued_business': issued,
                    'pending_business': pending,
                    'new_cases': new_cases,
                })
            for manager in self.object.get_managers():
                total, issued, pending, new_cases = salesperson_business_summary(
                    transactions,
                    manager)
                managers_business.append({
                    'name': manager,
                    'total_business': total,
                    'issued_business': issued,
                    'pending_business': pending,
                    'new_cases': new_cases,
                })

            return {'team_members': dsf_business, 'managers': managers_business}
        else:
            return {'team_members': None, 'managers': None}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.object.name}'
        context['transactions'] = self.get_transactions()
        context.update(self.business())
        context.update(**self.dsf_business())
        return context


class SalesPersonCreate(LoginRequiredMixin, CreateView):
    model = SalesPerson
    form_class = SalesPersonForm
    template_name = 'pqftl/add_update_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Add new Salesperson'
        return context


class SalesPersonUpdate(LoginRequiredMixin, UpdateView):
    model = SalesPerson
    form_class = SalesPersonForm
    template_name = 'pqftl/add_update_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Update {self.object.name} Details'
        return context


class SalesPersonDelete(LoginRequiredMixin, DeleteView):
    model = SalesPerson
    success_url = reverse_lazy('salesperson_list')
    template_name = 'pqftl/confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Delete {self.object.name}'
        return context


# Designation Views here
# Designation Views Here
class DesignationList(LoginRequiredMixin, ListView):
    model = Designation
    context_object_name = 'designations'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'All Titles'
        return context


class DesignationDetail(LoginRequiredMixin, DetailView):
    context_object_name = 'designation'
    model = Designation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.object.name} Title'
        return context


class DesignationCreate(LoginRequiredMixin, CreateView):
    model = Designation
    form_class = DesignationForm
    template_name = 'pqftl/add_update_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Add new Title'
        return context


class DesignationUpdate(LoginRequiredMixin, UpdateView):
    model = Designation
    form_class = DesignationForm
    template_name = 'pqftl/add_update_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Update {self.object.name} Title'
        return context


class DesignationDelete(LoginRequiredMixin, DeleteView):
    model = Designation
    success_url = reverse_lazy('designation_list')
    template_name = 'pqftl/confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Delete {self.object.name} Title'
        return context
