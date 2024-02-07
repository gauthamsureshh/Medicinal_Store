from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request,'index.html')

def loginpage(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('homepage')
        else:
            form = SignupForm()
        return render(request, 'signup.html', {'form': form})
    
def signout(request):
    logout(request)
    return redirect('homepage')

def userpage(request):
    return(request,'user.html')