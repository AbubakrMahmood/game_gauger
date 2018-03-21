import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'game_gauger.settings')

import django
django.setup()
from reviews.models import Game, Reviews

def populate();
    # list of dictionaries containing reviews to add to each game
    batman_arkham = [
        {"user_name" : "Bob",
         "comment" : "This is a comment",
         "rating" : "3"} ]

    games = {"Batman: Arkam Asylum":{"reviews":batman_arkham} }

    # goes through the games dictionary, then adds each game,
    # and then adds all the associated reviews for that game
    for game, game_data in games.items():
        g = add game()
        for r in game_data["reviews"]:
            add_review(g, r["user_name"], r["comment"], r["rating"])

    # Print out the games we have added
    for g in Game.objects.all():
        for r in Reviews.objects.filter(game=g):
            print("- {0} - {1}".format(str(g), str(r)))


def add_review(game, user_name, comment, rating=0):
    r = Reviews.objects.get_or_create(game=game)[0]
    r.user_name = user_name
    r.comment = comment
    r.rating = rating
    r.save()
    return r

def add_game(name, genre, publisher, developer, image):
    g = Game.objects.get_or_create(name=name, genre=genre, publisher=publisher
                                   developer=developer, image=image)[0]
    g.save()
    return g

if __name__ == '__main__':
    print("Starting Review population script...")
    populate()



