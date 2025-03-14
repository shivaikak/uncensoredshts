from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ToiletRanking
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

def submit_ranking(request):
    """API to submit a ranking"""
    if request.method == 'POST':
        data = json.loads(request.body)
        user = request.user
        toilet_name = data.get("toilet_name")
        rating = data.get("rating")
        review = data.get("review", "")

        if not (1 <= rating <= 5):
            return JsonResponse({"error": "Rating must be between 1 and 5"}, status=400)

        ranking = ToiletRanking.objects.create(
            user=user,
            toilet_name=toilet_name,
            rating=rating,
            review=review
        )
        return JsonResponse({"message": "Ranking submitted", "id": ranking.id}, status=201)

def get_rankings(request):
    """API to fetch all rankings"""
    rankings = ToiletRanking.objects.all().values('toilet_name', 'rating', 'review', 'user__username')
    return JsonResponse(list(rankings), safe=False)

