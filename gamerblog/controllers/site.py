import time
import json
from django.shortcuts import render
from django.http import HttpResponseRedirect
from base import get_base_url


def error_page(request):
    data = {
        'base_url': get_base_url()
    }

    return render(request, '404.html', data)


def server_error(request):
    data = {
        'base_url': get_base_url()
    }

    return render(request, '500.html', data)


def home(request):
    data = {
        'base_url': get_base_url()
    }

    return render(request, 'home.html', data)


def about(request):
    data = {
        'base_url': get_base_url()
    }

    return render(request, 'about.html', data)


def blog(request, blog_name):
    data = {
        'base_url': get_base_url()
    }

    blog_name = blog_name.strip().lower().replace('-', '_')

    return render(request, blog_name + '.html', data)
