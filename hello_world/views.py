from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    template = "index.html"

    context = {
        'test_text': "views.pyからアサインしたデータ",
    }
 
    return render(request, template, context)