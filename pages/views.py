from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    context={
        "text" : "my title",
        "number" : [123, 546, 121]
    }
    return render(request, 'home.html', context)