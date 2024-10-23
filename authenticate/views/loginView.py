from authenticate.views import *
from django.shortcuts import render

def login(request):
    pass
    return render(request, template_name='users/login.html'status=200)