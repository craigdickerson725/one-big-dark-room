from django.shortcuts import render


def handler404(request, exception):
    """Error 404 Page not found"""
    return render(request, "404.html", status=404)
