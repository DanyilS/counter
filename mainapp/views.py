from django.shortcuts import render

from .models import Count
# Create your views here.

def increment_counter(request):
    obj = Count.objects.first()
    obj.counter += 1
    obj.save()
    return render(request, 'index.html', context={'counter': obj.counter})