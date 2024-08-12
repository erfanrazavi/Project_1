from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

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
                form.add_error(None, 'نام کاربری یا رمز عبور نادرست است.')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'account/login.html', context)

@login_required
def logout_views(request):
    logout(request)
    return redirect('/')

def register_views(request):
    return render(request , 'account/register.html')