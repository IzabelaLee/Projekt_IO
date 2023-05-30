from django.shortcuts import render
from plants.models import Category, Plants

def index(request):
    plants = Plants.objects.all()
    categories = Category.objects.all()
    return render(request, 'core/index.html',{
        'categories' : categories,
        'plants' : plants,
    })

def contact(request):
    return render(request, 'core/contact.html')