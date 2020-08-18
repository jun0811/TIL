from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')




def dtl_example(request):
    meuns = ["짜장면", "탕수육", "양장피"]
    my_sentence = "life is short, you need python"
    message = ["apple", "banana, mango", "watermelon"]
    datetime_now = datetime.now()
    empty_list = []
    context = {
        "menus" : meuns,
        "my_sentence": my_sentence,
        "message" : message,
        "datetime_now" : datetime_now,

    }
    return render(request, 'articles/dtl_example.html', context)



def throw(request):
    return render(request, 'articles/throw.html')



def catch(request):
    username = request.GET.get("username")
    print(username)
    context = {
        "username" : username
    }

    return render(request,'articles/catch.html',context)