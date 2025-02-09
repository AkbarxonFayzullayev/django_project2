from django.http import HttpResponse


def funcn1(request):
    return HttpResponse("Salom django")