from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Nurtas")

def contact(request):
    return HttpResponse("Contacts: Nurtas")

def about(request):
    return HttpResponse("Nurtas very умный people")
