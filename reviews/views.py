from django.shortcuts import render
from django.http import HttpResponse
from reviews.models import Game

# Create your views here.
def index(request):
    game_list = Game.objects.all()
    context_dict = {'games': game_list}
    return render(request, 'reviews/index.html', context=context_dict)

def about(request):
    return render(request, 'reviews/about.html')

def featured(request):
    return render(request, 'reviews/featured.html')

def FAQs(request):
    return render(request, 'reviews/FAQ.html')

def categories(request):
    return render(request, 'reviews/categories.html')

def signinsignup(request):
    return render(request, 'reviews/signinsignup.html')

def addgame(request):
    return render(request, 'reviews/addgame.html')
