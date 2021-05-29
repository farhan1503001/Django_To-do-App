from django.shortcuts import render
from .models import List
from .forms import Listview
from django.contrib import messages #Importing to show message
# Create your views here.
def home(request):
    #Conditioning by reading request 
    if request.method=='POST':
        form=Listview(request.POST or None)
        if form.is_valid():
            form.save() 
            all_items=List.objects.all
            return render(request,'home.html',{'allitems':all_items})
    else:
         #Reading the database
        all_items=List.objects.all
        return render(request,'home.html',{'allitems':all_items})
def about(request):
    return render(request,'about.html',{})