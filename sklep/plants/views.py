from django.shortcuts import render, get_object_or_404
from .models import Plants

# Create your views here.
def detail(request, pk):
    plants = get_object_or_404(Plants, pk=pk)

    return render(request, 'plants/detail.html',{
        'plants': plants
    })
