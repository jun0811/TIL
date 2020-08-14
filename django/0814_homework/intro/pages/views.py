import random
from django.shortcuts import render

# Create your views here.

def lotto(request):
    numbers = range(1,46)
    nums = random.sample(numbers,6)
    context = { 
        'nums' : nums
    }
    
    return render(request, 'lotto.html', context)