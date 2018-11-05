from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  pass

# Game data with it's respective information
class Game(models.Model):
  name = models.CharField("The name of the game", max_length=50)
  franchise = models.CharField("The franchise of the game", max_length=50)
  publisher = models.CharField("The Publisher of the game", max_length=50) # TODO publisher must be a model with games list
  rating = models.DecimalField("Users rating of the game from 1 to 10", max_digits=3, decimal_places=1)
  rating_count = models.IntegerField("number of times this review has been voted (used to calculate review_rating)")
  overview = models.TextField("Quick description of the game",max_length=400)
  genres = models.ManyToManyField('Genre',blank=True)
  reviews = models.ManyToManyField('Review',blank=True)
  
  class Meta:
    db_table = 'games'
    managed = True
    ordering = ['name']
    verbose_name = 'game'
    verbose_name_plural = 'games'
  
  def __str__(self):
    return self.name+'('+str(self.pk)+')'

# A Genre of games, a way to categorize different games 
class Genre(models.Model):
  name = models.CharField(max_length=50)
  games = models.ManyToManyField('Game',through=Game.genres.through,blank=True)

  class Meta:
    db_table = 'Genres'
    managed = True
    ordering = ['name']
    verbose_name = 'genre'
    verbose_name_plural = 'genres'
    
  def __str__(self):
    return self.name

class Review(models.Model):
  title = models.CharField(max_length=50)
  content = models.TextField("Text of the review",max_length=20000)
  autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  game_rating = models.DecimalField("Review rating of the game from 1 to 10", max_digits=3, decimal_places=1)
  review_rating = models.DecimalField("rating of the raview from 1 to 10", max_digits=3, decimal_places=1)
  review_rating_count = models.IntegerField("number of times this review has been voted (used to calculate review_rating)")

  class Meta:
    db_table = 'Reviews'
    managed = True
    ordering = ['autor']
    verbose_name = 'review'
    verbose_name_plural = 'reviews'

  def __str__(self):
    return self.title+' ['+self.game_rating+']'









