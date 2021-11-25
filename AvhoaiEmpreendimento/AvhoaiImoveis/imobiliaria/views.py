from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    template_name = 'index.html'
    return render(request, template_name)

def corretor_list(request):
    template_name = 'corretor/corretor_list.html'
    objects = Corretor.objects.all()
    context = {'objects_list': objects}
    return render(request, template_name, context)

def corretor_detail(request, pk):
    template_name = 'corretor/corretor_detail.html'
    obj = Corretor.objects.get(pk=pk)
    context = {'object': obj }
    return render(request, template_name, context)
