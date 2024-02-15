from django.shortcuts import render
from django.http import HttpResponse

# views here:
def MainApp(request):
    return render(request, 'base.html')