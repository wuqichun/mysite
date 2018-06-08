from django.shortcuts import render, render_to_response
from .models import manage_ad


def index(request):
    alllist = manage_ad.objects.all()

    return render_to_response('delad/index.html',{"alllist":alllist})

# Create your views here.

def edit(request):

    print("-----------------------------")
    return None