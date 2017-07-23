from django.shortcuts import HttpResponse,render,redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index page.")

def login(request):
    return render(request, 'polls/SigninTemp.html')
    
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(':)')
    else:
        form = SignUpForm()
        
    return render(request, 'polls/signup.html', {'form': form})

def post(request):
    return render(request, 'polls/profTemp.html')