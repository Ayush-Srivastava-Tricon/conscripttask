from django.shortcuts import render,redirect
from .models import Student
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def index(request):

    return render(request,"index.html")

def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST["username"]
        password = request.POST["password"]


        user = User.objects.create_user(username=username,password=password)

        user.first_name = name
        user.save()

        return redirect("/")

    return render(request,"register.html")

def handlelogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        myuser = authenticate(username=loginusername, password=loginpassword)
        if myuser is not None:
          request.session["userinfo"] = loginusername
          login(request, myuser)

          messages.success(request,"Successfully Logged in")
          return redirect("/studentuser/")

        messages.error(request,"Invalid Credential")
        return redirect("/")


    return render(request,"index.html")

def handlelogout(request):
    if 'userinfo' in request.session:
        del (request.session['userinfo'])
        logout(request)
        messages.info(request,"Logged out")
        return redirect("/")

def studentuser(request):
    if request.method == "POST":
        s_name = request.POST.get("s_name")
        c_name = request.POST.get("c_name")
        specialisation = request.POST.get("specialisation")
        degree = request.POST.get("degree")
        intern = request.POST.get("intern")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        notes = request.POST.get("notes")

        stu = Student(s_name=s_name, c_name=c_name, specialisation=specialisation, degree=degree, intern=intern, phone = phone, email = email, gender = gender, notes = notes)
        stu.save()

        messages.success(request,"Successfully Detailes Submiited")
        return redirect("/studentuser/")


    return render(request,"studentuser.html")


def viewdetails(request):

     username = request.session["userinfo"]
     if request.session["userinfo"]==username:

         stu = Student.objects.filter(id=request.user.id)
         detail = {"details": stu}
         return render(request, "viewdetails.html", detail)



