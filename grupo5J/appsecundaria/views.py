from django.shortcuts import render
from .models import alumnoT, Frase
# Create your views here.
def Index_vista(request):
    misalumnos=alumnoT.objects.all().order_by("id")
    return render(request,"index.html",{"misalumnos":misalumnos})