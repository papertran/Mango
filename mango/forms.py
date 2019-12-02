from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from mango.models import userAccount, Account, Transactions

# Register user
class registrationForm(UserCreationForm):
    email = forms.EmailField(max_length=128, help_text="Required. Add a valid email addresss")

    class Meta:
        model = userAccount
        fields = ("email", "username","first_name", "last_name", "password1", "password2")

# Log user in
class loginForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model = userAccount
        fields = ('email', 'password')
    
    def clean(self):
        if self.is_valid:
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")

class accountUpdateForm(forms.ModelForm):
    class Meta:
        model = userAccount
        fields = ('email', 'username')

    def clean_email(self):
        if self.is_valid:
            email = self.cleaned_data['email']
            try:
                # Check if account exists
                account = userAccount.objects.exclude(pk=self.instance.pk).get(email=email)
            except userAccount.DoesNotExist:
                return email
            raise forms.ValidationError("Email {} is already in use".format(account.email))

    def clean_username(self):
        if self.is_valid:
            username = self.cleaned_data['username']
            try:
                # Check if account exists
                account = userAccount.objects.exclude(pk=self.instance.pk).get(username=username)
            except userAccount.DoesNotExist:
                return username
            raise forms.ValidationError("Email {} is already in use".format(account.username))

class addAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ("account_name", "account_type")

class addTransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ("transaction_name", "transaction_amount", "transaction_location", "transaction_date", "account", "category")
        widgets = {
            'transaction_date' : forms.DateInput(attrs={'type':'date'})
        }

class queryForm(forms.Form):
    startDate = forms.DateField(label="Start Date", widget=forms.DateInput(attrs={'type':'date'}), required=True)
    endDate = forms.DateField(label="Start Date", widget=forms.DateInput(attrs={'type':'date'}), required=True)
    Min = forms.DecimalField(decimal_places=2, required=True)
    Max = forms.DecimalField(decimal_places=2, required=True)