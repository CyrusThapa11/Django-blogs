from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


# Create your views here.

def index(req):
    response = render_to_string('challenges/challenges.html')
    return HttpResponse(response)


def jan():
    return ("working :!")


def feb():
    return ("working : 1")


def monthly_challenge_int(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):

    print(request)

    # month = 'january'
    text = None

    if month == 'january':
        text = jan()
    elif month == 'february':
        text = feb()
    else:
        return HttpResponse("Not found")

    return HttpResponse(text)
