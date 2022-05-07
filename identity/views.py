from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.urls import reverse_lazy
from django.contrib import messages
from shop.models import Customer
from .models import Profile




def login_view(request):
    error_message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('home')
        error_message = "Username or password does not exist"

    return render(request, 'identity/login.html', {error_message: error_message})

def signup_view(request):
    
    if request.method == "POST":
     form = SignUpForm(request.POST)
     if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        email = request.POST.get('email')
        user = authenticate(username=username, password=password)
        Customer.objects.create(user=user,name=username,email=email) 
       
        
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'identity/signup.html', {
        'form': form
        })


def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'identity/profile.html', context)


#  def logout_view(request):
#      if request.method == "POST":
#       form = SignUpForm(request.POST)
#       if form.is_valid():
#          form.save()
#          username = form.cleaned_data['username']
#          password = form.cleaned_data['password1']
#          email = request.POST.get('email')
#          user = authenticate(username=username, password=password)
#          Customer.objects.create(user=user,name=username,email=email) 
       
        
#          login(request, user)
#          return redirect('home')
#      else:
#          form = SignUpForm()

#      return render(request, 'identity/signup.html', {
#          'form': form
#          })