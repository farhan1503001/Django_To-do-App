from django.shortcuts import render
from .models import List
from .forms import Listview
# Create your views here.
def home(request):
    #Conditioning by reading request 
    if request.method=='POST':
        form=Listview(request.POST or None)
        if form.is_valid():
            form.save() 
            all_items=List.objects.all
            return render(request,'home.html',)
    else:
         #Reading the database
        all_items=List.objects.all
        return render(request,'home.html',{'allitems':all_items})
def about(request):
    return render(request,'about.html',{})