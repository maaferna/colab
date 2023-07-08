from django.shortcuts import render

# Create your views here.

def v_index(request):
    context = {}
    return render(request, 'index.html', context)