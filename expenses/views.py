from django.shortcuts import render


from django.http import HttpResponse

from expenses.models import Expense


def expense_list(request):
    return render(request, "expenses/expenses_list.html", {
        'y': Expense.objects.all(),
    })

def index(request):
    return HttpResponse("Hello, exspenses")

