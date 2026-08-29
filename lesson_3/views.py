from django.shortcuts import render
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from django.templatetags.static import static

def main(request):
    return render(request, 'main.html')