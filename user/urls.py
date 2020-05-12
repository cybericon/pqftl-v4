from django.urls import path
from . import views

urlpatterns = [
    # SalesPerson Urls
    path('salespersons/', views.SalesPersonList.as_view(), name='salesperson_list'),
    path('salesperson/<int:pk>/', views.SalesPersonDetail.as_view(),
         name='salesperson_detail'),
    path('salesperson/add/', views.SalesPersonCreate.as_view(),
         name='salesperson_add'),
    path('salesperson/<int:pk>/update',
         views.SalesPersonUpdate.as_view(), name="salesperson_update"),
    path('salesperson/<int:pk>/delete',
         views.SalesPersonDelete.as_view(), name="salesperson_delete"),
    # Designation Urls
    path('designations/', views.DesignationList.as_view(), name='designation_list'),
    path('designation/<int:pk>/', views.DesignationDetail.as_view(),
         name='designation_detail'),
    path('designation/add/', views.DesignationCreate.as_view(),
         name='designation_add'),
    path('designation/<int:pk>/update',
         views.DesignationUpdate.as_view(), name="designation_update"),
    path('designation/<int:pk>/delete',
         views.DesignationDelete.as_view(), name="designation_delete"),
]
