from django.shortcuts import render
from django.http import HttpResponse

def hello_view(request):
    return HttpResponse('Say Hello to my little Test app!')
# in the browser go to the address - http://localhost:8000/Testapp/hello/

def classroom_task(request):
    return HttpResponse('Hello my neighbours! F*ck you too!!!')

def my_landing_page(request):
    return render(request, 'landing_page.html')

