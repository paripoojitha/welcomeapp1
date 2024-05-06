from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    res=HttpResponse("""<html><body bgcolor=pink><center>
    <h1>welcome to poojitha</h1></center></body></html>""")
    return res

# Create your views here.
