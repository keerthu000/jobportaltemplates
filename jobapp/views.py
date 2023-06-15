from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def applyjob(request):
    return render(request,'applyjob.html')
def searchjob(request):
    return render(request,'searchjob.html')

    
    
