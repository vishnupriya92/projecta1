from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>hi how are u</h1>")