from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import QuerySet


class DesignationQueryset(QuerySet):
    pass


class Designation(models.Model):
    name = models.CharField(max_length=100)
    titles = DesignationQueryset.as_manager()

    def get_absolute_url(self):
        return reverse("designation_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class SalesPersonQueryset(QuerySet):
    def managers(self):
        return self.filter(is_manager=True).exclude(branch_name=None)

    def dsf(self):
        return self.filter(is_manager=False)


class SalesPerson(models.Model):
    name = models.CharField(max_length=200)
    branch_name = models.ForeignKey('location.Branch', related_name='branch_members',
                                    null=True, blank=True, on_delete=models.SET_NULL)
    designation = models.ForeignKey(
        Designation, related_name='are', null=True, blank=True, on_delete=models.SET_DEFAULT, default=1)
    is_manager = models.BooleanField(default=False)
    reporting_manager = models.ForeignKey(
        'self', related_name="team", null=True, blank=True, limit_choices_to={'is_manager': True}, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    persons = SalesPersonQueryset.as_manager()

    def get_absolute_url(self):
        return reverse("salesperson_detail", kwargs={"pk": self.pk})

    def get_personal_business(self):
        from business.models import Transaction
        return Transaction.records.filter(sales_person=self)

    def get_team_business(self):
        from business.models import Transaction
        return Transaction.records.filter(models.Q(sales_person__reporting_manager=self)) if self.is_manager else None

    def get_dsf(self):
        return self.team.dsf()

    def get_managers(self):
        return self.team.managers()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sales_person = models.OneToOneField(
        SalesPerson, on_delete=models.SET_NULL, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images')

    def __str__(self):
        return self.user.username
