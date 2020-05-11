from django.contrib import admin
from .models import Branch
# Register your models here.


class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch_head')
    list_editable = ('branch_head',)


admin.site.register(Branch, BranchAdmin)
