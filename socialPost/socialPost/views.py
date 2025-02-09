from django.http import HttpResponse
from django.shortcuts import render

def guide(request):
    # return HttpResponse('Hello, World!')
    return render(request, 'guide.html' )
