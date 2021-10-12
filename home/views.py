from django.shortcuts import render,redirect 
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate

# Create your views here.
def index(request):
   print(request.user)
   print("python")
   if request.user.is_anonymous:
      print("react")
      return redirect("/login")
   return render(request,'index.html')

def loginUser(request):
   if request.method=="POST":
      username = request.POST.get('username')
      password = request.POST.get('password')
      # check if user has entered correct credentials
      print(username,password)
      user = authenticate(username=username, password=password)

      if user is not None:
         # A backend authenticated the credentials
         login(request,user)
         # print("redux")
         return redirect("/")

      else:
         # NO backend authenticated the credentials
         # print("c++")
         return render(request,'login.html')

   return render(request,'login.html')          

def logoutUser(request):
   logout(request)
   return redirect("/login")

