from django.urls import path
from . import views

urlpatterns = [
    path('branches/', views.BranchList.as_view(), name='branch_list'),
    path('branch/<int:pk>/', views.BranchDetail.as_view(), name='branch_detail'),
    path('branch/add/', views.BranchCreate.as_view(), name='branch_add'),
    path('branch/<int:pk>/update',
         views.BranchUpdate.as_view(), name="branch_update"),
    path('branch/<int:pk>/delete',
         views.BranchDelete.as_view(), name="branch_delete"),

]
