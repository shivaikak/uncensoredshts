from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# view when registering for account
def register_view(request):
    # create user account upon data submission
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # verify and save to database
        if form.is_valid():
            user = form.save()
            login(request.user)
            return redirect('home')
    # GET request: display empty sign-up form 
    else:
        form = UserCreationForm()
    # render sign-up form
    return render(request, 'user_accounts/register.html', {'form': form})

# view when logging in        
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        # verify and log-in user
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    # GET request: display empty log-in form
    else:
        form = AuthenticationForm()
    # render log-in page
    return render(request, 'user_accounts/login.html', {'form': form})

# clear session
def logout_view(request):
    logout(request)
    return redirect('login')

