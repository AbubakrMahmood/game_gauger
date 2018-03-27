from django.db import models
import numpy as np
from django.contrib import admin
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.contrib.auth.models import User

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
    UID = models.IntegerField(default=0, unique=True)
    game = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    publisher = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    logo = models.ImageField(upload_to = 'media/', default = 'media/None/no-img.jpg')

    def save(self, *args, **kwargs):
    	#Opening the uploaded image
    	im = Image.open(self.logo)
    	output = BytesIO()

    	#Resize/modify the image
    	im = im.resize( (220,277) )

    	#after modifications, save it to the output
    	im.save(output, format='JPEG', quality=100)
    	output.seek(0)

    	#change the imagefield value to be the newley modifed image value
    	self.logo = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.logo.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
    	super(Game,self).save(*args, **kwargs)

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

class UserProfile(models.Model):
    # Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    
    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
        return self.user.username
