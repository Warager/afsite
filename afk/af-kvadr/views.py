from django.shortcuts import render


def home(request):
    """
    Renders home page
    """
    data = {
        "current_page": 'home'
    }
    return render(request, 'afcapp/home.html', data)


def about(request):
    """
    Renders home page
    """
    data = {
        "current_page": 'about'
    }
    return render(request, 'afcapp/about.html', data)


def scope(request):
    """
    Renders scope page
    """
    data = {
        "current_page": 'scope'
    }
    return render(request, 'afcapp/scope.html', data)


def contact(request):
    """
    Renders home page
    """
    data = {
        "current_page": 'contact'
    }
    return render(request, 'afcapp/contact.html', data)


def zurb(request):
    """
    Renders home page
    """
    return render(request, 'afcapp/zurb.html',)