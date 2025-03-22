from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model # Importing User model

User = get_user_model()

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') or None
        password = request.POST.get('password') or None
        if all([username, password]):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print('Login Here!')
                return redirect("/home")
    return render(request, 'auth/login.html', {})

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') or None
        email = request.POST.get('email') or None
        password = request.POST.get('password') or None
        if all([username, email, password]):
            # #Django Forms works really well with for this validation
            # # check if the user already exists in the db by importing the user model
            # username_exits_qs = User.objects.filter(username__iexact=username).exists()
            # email_exits_qs = User.objects.filter(email__iexact=email).exists()
            # # create user from the base user model?
            try:
                User.objects.create_user(username=username, email=email, password=password)
            except Exception as e:
                print(e)
                return redirect('auth/register.html')
            return redirect("/home")
    return render(request, 'auth/register.html', {})
        

# def register_view(request):
#     return render(request, 'auth/register.html', {})

