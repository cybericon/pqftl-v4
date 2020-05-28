from django.db import models
from django.urls import reverse
from django.db.models import QuerySet


class BranchQueryset(QuerySet):
    pass


class Branch (models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    branch_head = models.ForeignKey(
        'user.SalesPerson', limit_choices_to={'is_manager': True}, null=True, blank=True, on_delete=models.SET_NULL, related_name='branch')
    locations = BranchQueryset.as_manager()

    def get_absolute_url(self):
        return reverse("branch_list")

    def get_dsf(self):
        return self.branch_members.dsf()

    def get_managers(self):
        return self.branch_members.managers()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'branch'
        verbose_name_plural = "branches"
