from django.shortcuts import render

# Create your views here.


def dinner(request, menu, x):
    context = {
        'menu' : menu,
        'x' : x
    }
    return render(request, 'dinner.html', context)