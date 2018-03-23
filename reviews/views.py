from django.shortcuts import render
from django.http import HttpResponse
from reviews.models import Game, Review

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

#def show_game(request, game_name_slug):
#    context_dict = {}
#
#    try:
#        game = Game.objects.get(slug=game_name_slug)
#
#
#        reviews = Review.objects.filter(game=game)
#        context_dict['reviews'] = reviews
#        context_dict['game'] = game
#
#    except Game.DoesNotExist:
#        context_dict['game'] = None
#        context_dict['reviews'] = None
#
#    return render(request, 'rango/game.html', context_dict)
