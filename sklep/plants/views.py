from django.shortcuts import render, get_object_or_404
from .models import Plants

def detail(request, pk):
    plants = get_object_or_404(Plants, pk=pk)

    related_plants = Plants.objects.filter(category=plants.category).exclude(pk=pk)[0:10]


    return render(request, 'plants/detail.html', {
        'plants':plants ,
        'related_plants' : related_plants})
    
def index(request):
    return render(request, 'core/index.html')