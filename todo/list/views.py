from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import Register,Signin,person_list
from django.contrib import messages
from .models import todo
# Create your views here.

#In SignIn function we just see that the login credentials are proper or not and let the user login on that basis
def SignIn(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('display')
        else:
            messages.warning(request,"Invalid Login")
            sign=Signin()
            return render(request,'sign.html',{'message':messages,'signin':sign})
    else:
        sign=Signin()
        return render(request,'sign.html',{'signin':sign})

#The register function deals with reisteration details and if all details are valid redirects to login page
def register(request):
    if request.method == 'POST':
        registeration=Register(request.POST)
        if registeration.is_valid():
            registeration.save()
            return redirect('signin')
        else:
            messages.warning(request,"Invalid Details")
            registeration=Register()
            return render(request,'registeration.html',{'register':registeration,'message':messages})
    else:
        registeration=Register()
        return render(request,'registeration.html',{'register':registeration})

#This is How Welcome page look
def display_page(request):
    if request.method=="POST":
        return redirect('list')
    else:
        Name2=request.user
        obj=todo.objects.filter(name=request.user)
        return render(request,'welcome.html',{'Name':Name2,'obj':obj})

#This def just takes the input for list and redirects to home page 
def list(request):
    if request.method=="POST":
      f3=person_list(request.POST)
      if f3.is_valid():
            Data=todo()
            Data.Title=f3.cleaned_data['Title']
            Data.Note=f3.cleaned_data['Note']
            Data.Last_Date=f3.cleaned_data['Last_Date']
            Data.Count=f3.cleaned_data['Count'] 
            Data.Status=f3.cleaned_data['Status']
            Data.name=request.user 
            Data.save()
            return redirect('display')
      else:
            f3=person_list()
            return render(request,'list.html',{'list':f3})

    else:
        f3=person_list()
        return render(request,'list.html',{'list':f3})

#This def logs out from server
def signout(request):
    logout(request)
    return redirect('signin')

#This Updates the data if needed
def update(request,id):
    if request.method=="POST":
        pi=todo.objects.get(pk=id)
        f3=person_list(request.POST,instance=pi)
        if f3.is_valid():
            Data=todo.objects.get(pk=id)
            Data.Title=f3.cleaned_data['Title']
            Data.Note=f3.cleaned_data['Note']
            Data.Last_Date=f3.cleaned_data['Last_Date']
            Data.Count=f3.cleaned_data['Count'] 
            Data.Status=f3.cleaned_data['Status']
            Data.name=request.user 
            Data.save()
            return redirect('display')
    else:
        pi=todo.objects.get(pk=id)
        f3=person_list(instance=pi)
        return render(request,'update.html',{'list':f3,'id':pi})

#This one gets the Instance and deletes that list and returns back to display page
def delete(request,id):
    if request.method=="POST":
        pi=todo.objects.get(pk=id)
        pi.delete()
        return redirect('display')


