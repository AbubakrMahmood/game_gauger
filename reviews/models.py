from django.db import models
import numpy as np
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify

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


class Categories(models.Model):
  categories = models.CharField(max_length=17, choices=Genre_list, default='Please Select')

class Game(models.Model):
    game = models.CharField(max_length=100, unique = True)
    genre = models.CharField(max_length=30)
    publisher = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    logo = models.ImageField(upload_to = 'media/', default = 'None/no-img.jpg')
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.game)
        super(Game, self).save(*args, **kwargs)

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __str__(self):
        return self.game

    def __unicode__(self):
        return self.game

RATING_CHOICES=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
)

class Review(models.Model):

    game = models.ForeignKey(Game)
    comment_date = models.DateTimeField(auto_now=True)
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=2000)
    rating = models.IntegerField(choices=RATING_CHOICES)

class UserProfile(models.Model):
    # Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

