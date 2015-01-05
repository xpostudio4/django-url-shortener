from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect


def create(request):
    """This url is only to create new short urls"""
    pass

def follow(request, shortened_id):
    """This process a shortened url in the page"""
    pass

def index(request):
    """This one is the main page and contains the forms and all the urls created"""
    pass

