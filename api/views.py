from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# endpoints: url in our site
def main(request):
    return HttpResponse("<h1>Hello Django</h1>")