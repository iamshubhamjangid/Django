from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.shortcuts import render

def index(request):
    return render(request, 'default/index.html', {})	

