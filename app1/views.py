from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 

# Create your views here.
def indexpage(request):
    return render(request,'index.html')
    
def registration(request):
    if request.method=="POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not saame ")

        my_user = User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')
        

    return render(request,'registration.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1=request.POST.get('pass')
        user = authenticate(request,username=username,password = pass1)
        if user is not None:
            login(request,user)
            return redirect('indexpage')
        else:
            return HttpResponse("Username or Password is incorrect!")
    return render(request,'login.html')