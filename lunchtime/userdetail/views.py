from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.

@login_required
def loginUserPage(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        # try:
        #     user = User.objects.get(username=username)
        # except:
        #     messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request, 'Username or password is incorrect!')

    return render(request, 'users/login_register.html')
