from django.shortcuts import redirect, render
from .models import List
from .forms import Listview
from django.contrib import messages #Importing to show message
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    #Conditioning by reading request 
    if request.method=='POST':
        form=Listview(request.POST or None)
        if form.is_valid():
            form.save() 
            all_items=List.objects.all
            messages.success(request,'Item has been added to list')
            return render(request,'home.html',{'allitems':all_items})
    else:
         #Reading the database
        all_items=List.objects.all
        return render(request,'home.html',{'allitems':all_items})
def about(request):
    return render(request,'about.html',{})
def delete(request,id):
    item=List.objects.get(pk=id)
    item.delete()
    #Showing message after delete
    messages.success(request,'Item Deleted From List')
    return redirect('home')
def change_status(request,id):
    item=List.objects.get(pk=id)
    if item.completed:
        item.completed=False
    else:
        item.completed=True
    item.save()
    messages.success(request,'Updated Status')
    return redirect('home')
def edit(request,id):
    if request.method=='POST':
        if request.method=='POST':
            form=Listview(request.POST or None)
            if form.is_valid():
                form.save() 
                all_items=List.objects.all
                messages.success(request,'Item Edited Successfully')
                return render(request,'home.html',{'allitems':all_items})
    else:
        item=List.objects.item
        return render(request,'edit.html',{'item':item})
