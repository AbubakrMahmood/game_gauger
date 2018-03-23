from django.db import models
import numpy as np
from django.contrib import admin


Genre_list=( ("","Please Select"),
    ('ACTION','Action'),
    ('ACTIONADVENTURE','Action-Adventure'),
    ('ADVENTURE','Adventure'),
    ('MISC','Misc'),
    ('RPG','Role-Playing Game'),
    ('SIMULATION','Simulation'),
    ('STRATEGY','Strategy'),
    ('SPORTS','Sports'),
    ('PUZZLE','Puzzle'),

)

class Game(models.Model):
    game = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    publisher = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'media/', default = 'media/None/no-img.jpg')
    #slug = models.SlugField(unique=True)

    #def save(self, *args, **kwargs):
    #    self.slug = slugify(self.game)
     #   super(Game, self).save(*args, **kwargs)
    
    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)
    
    def __str__(self):
        return self.game

    def __unicode__(self):
        return self.game


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    game = models.ForeignKey(Game)
    comment_date = models.DateTimeField(auto_now=True)
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=2000)
    rating = models.IntegerField(choices=RATING_CHOICES)

