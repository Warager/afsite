from django.shortcuts import render


def home(request):
    """
    Renders home page
    """
    data = {
        "current_page": 'home'
    }
    return render(request, 'af-kvadr/home.html', data)


def about(request):
    """
    Renders home page
    """
    data = {
        "current_page": 'about'
    }
    return render(request, 'af-kvadr/about.html', data)


def scope(request):
    """
    Renders scope page
    """
    data = {
        "current_page": 'scope'
    }
    return render(request, 'af-kvadr/scope.html', data)


def contact(request):
    """
    Renders home page
    """
    data = {
        "current_page": 'contact'
    }
    return render(request, 'af-kvadr/contact.html', data)


def zurb(request):
    """
    Renders home page
    """
    return render(request, 'af-kvadr/zurb.html',)