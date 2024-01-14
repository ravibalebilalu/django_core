from django.shortcuts import render,redirect
from .models import receipe
from django.http import HttpResponse

def reciepes(request):
    if request.method == "POST":
        data = request.POST
        receipe_id = data.get("receipe.id")
        receipe_name = data.get("receipe_name")
        receipe_decription = data.get("receipe_decription")
        receipe_image = data.get("receipe_image")
        
        receipe.objects.create(id=receipe_id,receipe_name=receipe_name,receipe_decription=receipe_decription,receipe_image=receipe_image)
     
    query_set = receipe.objects.all()
    context = {"receipe":query_set}
    return render(request,'reciepes.html',context)

def delete_receipe(request,id):
    query_set = receipe.objects.get(id = id)
    query_set.delete()
    return redirect("/reciepes/")


def update_receipe(request,id):
    query_set = receipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        receipe_id = data.get("receipe.id")
        receipe_name = data.get("receipe_name")
        receipe_decription = data.get("receipe_decription")
        receipe_image = data.get("receipe_image")

        query_set.receipe_name = receipe_name
        query_set.receipe_decription = receipe_decription
        query_set.receipe_name = receipe_name

        query_set.save()
        return redirect("/reciepes/")

    context = {"receipe":query_set}
    return render(request,"update_receipe.html",context)