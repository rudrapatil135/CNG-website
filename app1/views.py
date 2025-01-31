from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User

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
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1=request.POST.get('pass')
    return render(request,'login.html')