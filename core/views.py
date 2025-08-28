from django.shortcuts import render

def home(request):
    return render(request,"core/home.html")

def gallery(request):
    return render(request,"core/gallery.html")

def informacion(request):
    return render(request,'core/informacion.html')

def historia(request):
    return render(request,'core/historia.html')
