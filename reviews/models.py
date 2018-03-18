from django.db import models
import numpy as np


class Game(models.Model):
    name = models.CharField(max_length=100, unique=True)
    genre = models.CharField(max_length=20)
    publisher = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'media/', default = 'media/None/no-img.jpg')
    
    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)
        
    def __unicode__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    game = models.ForeignKey(Game)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=2000)
    rating = models.IntegerField(choices=RATING_CHOICES)
