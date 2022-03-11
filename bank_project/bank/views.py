from django.shortcuts import render
from .models import Account
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.method == "POST":
        account_name = request.POST["account_name"]

        account = Account()
        account.user = request.user
        account.account_name = account_name
        account.save()

    accounts = Account.objects.filter(user=request.user)
    context = {
        'accounts': accounts
    }
    return render(request, 'bank/index.html', context)

