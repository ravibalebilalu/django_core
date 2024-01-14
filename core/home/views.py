from django.shortcuts import render

from django.http import HttpResponse

def home(request):
 
     
    context = {"page":"home"}
    return render(request,'index.html',context)

    
def about(request):
    context = {"page":"about"}
    return render(request,'about.html',context)


def contact(request):
    context = {"page":"contact"}
    return render(request,'contact.html',context)