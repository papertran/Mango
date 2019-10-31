from django.shortcuts import render, redirect
from mango.models import userAccount, Account, Transactions
from mango.forms import registrationForm
from django.contrib.auth import login, authenticate
from django.views import View

# Create your views here.
def index(request):
    return render(request, 'mango/index.html')

def register(request):
    context = {}
    if request.POST:
        form = registrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('index')
        else:
            context['registration_form'] = form
    else:
        form = registrationForm()
        context['registration_form'] = form
    return render(request, 'mango/register.html', context=context)
