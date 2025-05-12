from django.shortcuts import render
# This code is basically creating what the user is viewing on their end of the interface i.e. transactions
# Create your views here.
from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm

# View to list all transactions
def transaction_list(request):
    transactions = Transaction.objects.order_by('-date')
    return render(request, 'tracker_app/transaction_list.html', {'transactions': transactions})

# View to add a new transaction
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'tracker_app/add_transaction.html', {'form': form})