from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def login_views(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, 'please enter correct email or user name')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    
    return render(request, 'account/login.html', context)

@login_required
def logout_views(request):
    logout(request)
    return redirect('/')

def register_views(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('accounts:login'))
    
        form = UserCreationForm()
        context = {'form' : form}
        return render(request , 'account/register.html', context)
    else:
        return redirect('/')