from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def goods(request):
    return HttpResponse('На этой странице будут отображаться продукты. Может быть... Когда-нибудь...')
