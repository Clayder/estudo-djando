from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá")


def detail(request, question_id):
    return HttpResponse("Retornando perguntas pelo id: %s." % question_id)


def results(request, question_id):
    response = "Resultados da pergunta %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Você está votando na pergunta %s" % question_id)

