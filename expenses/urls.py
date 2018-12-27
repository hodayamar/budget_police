from django.urls import path

from expenses.views import expense_list, index
from . import views

urlpatterns = [
    path('', index),
    path('expense_list',expense_list),
]