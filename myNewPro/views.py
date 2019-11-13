from django.shortcuts import render, HttpResponse


def mainIndex(request):
    return render(request, 'index.html')