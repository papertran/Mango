from django.shortcuts import render, redirect
from mango.models import userAccount, Account, Transactions
from mango.forms import registrationForm, loginForm
from django.contrib.auth import login,logout, authenticate
from django.views import View

# Create your views here.
def index_view(request):
    return render(request, 'mango/index.html')

def register_view(request):
    context = {}
    if request.POST:
        form = registrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('mango:index')
        else:
            context['registration_form'] = form
    else:
        form = registrationForm()
        context['registration_form'] = form
    return render(request, 'mango/register.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('mango:index')

def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('mango:index')

    # User tried to login
    if request.POST:
        form = loginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('mango:index')
    else:
        form = loginForm()
    
    context['login_form'] = form
    return render(request, 'mango/login.html', context=context)