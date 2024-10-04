from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def homePage(request):
    if request.method=="POST":
        s1=request.POST.get("subject1")

    return render(request,"index.html")
def homePage1(request):
    if request.method=="POST":
        s1=request.POST.get("subject1")

    return render(request,"index2.html")
def homePage2(request):
    return render(request,"user_regis.html")
def homePage3(request):
    if request.method=="POST":
        s1=request.POST.get("subject1")

    return render(request,"patient_form.html")



def signUp(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

       
        if User.objects.filter(username=username).exists():
           
            return render(request, 'signup.html', {'error': 'Username already exists'})
        
      
        if password != confirm_password:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})

       
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('/login5')

    
    return render(request, 'patient_signup.html')


def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None: 
            auth.login(request, user) 
            return redirect('login2') 
        
    return render(request, "user_login.html")
def userDetail(request):
    if request.method=="POST":
        s1=request.POST.get("subject1")

    return render(request,"user_details.html")
def about(request):
    if request.method=="POST":
        s1=request.POST.get("subject1")

    return render(request,"aboutus.html")
def services(request):
    if request.method=="POST":
        s1=request.POST.get("subject1")

    return render(request,"services.html")
def doctors(request):
    if request.method=="POST":
        s1=request.POST.get("subject1")

    return render(request,"doctors.html")
def contacts(request):
    if request.method=="POST":
        s1=request.POST.get("subject1")

    return render(request,"contact.html")


