from django.shortcuts import render,redirect,HttpResponse
from .models import receipe
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
@login_required(login_url = "/login/")
def reciepes(request):
    if request.method == "POST":
        data = request.POST
        receipe_id = data.get("receipe_id")
        receipe_name = data.get("receipe_name")
        receipe_decription = data.get("receipe_decription")
        receipe_image = data.get("receipe_image")
        
        receipe.objects.create(id=receipe_id,receipe_name=receipe_name,receipe_decription=receipe_decription,receipe_image=receipe_image)
     
    query_set = receipe.objects.all()

    if request.GET.get('search'):
        query_set = query_set.filter(receipe_name__icontains = request.GET.get('search'))

    context = {"receipe":query_set}
    return render(request,'reciepes.html',context)
@login_required(login_url = "/login/")
def delete_receipe(request,id):
    query_set = receipe.objects.get(id = id)
    query_set.delete()
    return redirect("/reciepes/")

@login_required(login_url = "/login/")
def update_receipe(request,id):
    query_set = receipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        receipe_id = data.get("receipe.id")
        receipe_name = data.get("receipe_name")
        receipe_decription = data.get("receipe_decription")
        receipe_image = data.get("receipe_image")

        query_set.receipe_name = receipe_name
        query_set.receipe_decription = receipe_decription
        query_set.receipe_image = receipe_image

        query_set.save()
        return redirect("/reciepes/")

    context = {"receipe":query_set}
    return render(request,"update_receipe.html",context)

 

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username").strip()
        password = request.POST.get("password").strip()
        
        if not User.objects.filter(username=username).exists():
            messages.info(request, 'Invalid username!')
            
            return redirect("/login/")

        user = authenticate( username=username, password=password)
         

        if user is None:
            messages.info(request, 'Invalid Password!')
            return render(request, 'login.html')
        else:
            login(request, user)
            return redirect("reciepes")  
    return render(request, 'login.html')   

def log_out(request):
    logout(request)
    return redirect('/login/')
    

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name").strip()
        last_name = request.POST.get("last_name").strip()
        username = request.POST.get("user_name").strip()
        password = request.POST.get("password").strip()
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'username is already taken')
            return redirect("/register/")


        user = User.objects.create(
            first_name=first_name,
            last_name= last_name,
            username = username,
            email = ""

        )
        print(user)
        user.set_password(password)
        user.save()
        messages.info(request,'Account created succussfully!')
        return redirect('/register/')
    else:
        print("not getting")

    return render(request,'register.html')