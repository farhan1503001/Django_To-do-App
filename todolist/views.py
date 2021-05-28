from django.shortcuts import render
from .models import List
# Create your views here.
def home(request):
    #Reading the database
    all_items=List.objects.all
    return render(request,'home.html',{'allitems':all_items})
def about(request):
    return render(request,'about.html',{})