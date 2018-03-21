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
