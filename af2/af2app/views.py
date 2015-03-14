from django.shortcuts import render


def home(request):
    """
    Renders home page
    """
    data = {
        "current_page": 'home'
    }
    return render(request, 'af2app/home.html', data)


def about(request):
    """
    Renders home page
    """
    data = {
        "current_page": 'about'
    }
    return render(request, 'af2app/about.html', data)


def scope(request):
    """
    Renders scope page
    """
    data = {
        "current_page": 'scope'
    }
    return render(request, 'af2app/scope.html', data)


def contact(request):
    """
    Renders home page
    """
    data = {
        "current_page": 'contact'
    }
    return render(request, 'af2app/contact.html', data)


def zurb(request):
    """
    Renders home page
    """
    return render(request, 'af2app/zurb.html',)