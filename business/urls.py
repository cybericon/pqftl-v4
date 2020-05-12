from django.urls import path
from . import views

urlpatterns = [
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transaction/<int:pk>/', views.TransactionDetail.as_view(),
         name='transaction_detail'),
    path('transaction/add/', views.TransactionCreate.as_view(),
         name='transaction_add'),
    path('transaction/<int:pk>/update',
         views.TransactionUpdate.as_view(), name="transaction_update"),
    path('transaction/<int:pk>/delete',
         views.TransactionDelete.as_view(), name="transaction_delete"),
]
