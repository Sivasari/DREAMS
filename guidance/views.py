from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm, ProfileForm
from .models import UserProfile

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required




from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Career
from .serializers import CareerSerializer


from django.http import JsonResponse
from .models import Career
from .serializers import CareerSerializer

def career_recommendation(request):
    if request.method == 'GET':
        careers = Career.objects.all()
        serializer = CareerSerializer(careers, many=True)
        return JsonResponse(serializer.data, safe=False)

def home(request):
    return render(request,'guidance/home.html')




def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'guidance/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page or dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'guidance/login.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page or dashboard
    else:
        form = ProfileForm(instance=request.user.userprofile)
    return render(request, 'guidance/profile.html', {'form': form})


