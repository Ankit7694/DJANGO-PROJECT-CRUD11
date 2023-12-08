from django.shortcuts import render,redirect
from .models import Details
from django.urls import reverse
from .forms import detailsform
# Create your views here.

def member(request):
    return render(request,"index.html")

def registration(request):
    if request.method=="POST":
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            gender=request.POST['gender']
            obj =Details.objects.create(username = username,email=email,password=password,gender=gender)
            obj.save()
            
    return render(request,'index.html')

def retrieve(request):
    details=Details.objects.all()
    return render(request,'retrieve.html' ,{'details':details})

def edit(request,id):
    object=Details.objects.get(id=id)
    return render(request,"edit.html", {"object":object})

def update(request,id):
    object=Details.objects.get(id=id)
    form=detailsform(request.POST,instance=object)
    if form.is_valid:
        form.save()
        object=Details.objects.all()
        return redirect('/retrieve/')
    return render(request,"retrieve.html")

def delete(request,id):   
        obj=Details.objects.filter(id=id).delete()
        return render(request,'retrieve.html')  
