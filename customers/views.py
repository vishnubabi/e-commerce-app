from django.shortcuts import render

# Create your views here.
def account_views(request):
    return render(request, 'customers/account.html')
