from django.shortcuts import render
from django.http import HttpResponse


def main_site(request):
    return HttpResponse("simanoo")
