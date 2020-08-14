import requests
from django.shortcuts import render

# Create your views here.


def message(request):
    return render(request, 'message.html')


def api(request):
    name = request.GET.get('name')

    url = f'http://artii.herokuapp.com/make?text={name}'
    response = requests.get(url).text
    context = {
        'name' : response
    }
    return render(request, "api.html", context)
