from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser, models.Model):
  favourites = models.ForeignKey('Game',blank=True, null=True, on_delete=models.DO_NOTHING)
  reviews = models.ForeignKey('Review',blank=True, null=True, on_delete=models.CASCADE)
  pass

# Game data with it's respective information
class Game(models.Model):
  name = models.CharField("The name of the game", max_length=50)
  franchise = models.CharField("The franchise of the game", max_length=50)
  publisher = models.CharField("The Publisher of the game", max_length=50) # TODO publisher must be a model with games list
  score = models.DecimalField("Users rating of the game from 1 to 10", max_digits=3, decimal_places=1, default=0)
  votes = models.IntegerField("number of times this review has been voted (used to calculate review_rating)", default=0)
  overview = models.TextField("Quick description of the game",max_length=400)
  genres = models.ManyToManyField('Genre',blank=True, null=True)
  reviews = models.ManyToManyField('Review',blank=True, null=True)
  
  class Meta:
    db_table = 'games'
    managed = True
    ordering = ['name']
    verbose_name = 'game'
    verbose_name_plural = 'games'
  
  def get_rating(self):
    return self.score/self.votes

  def rate(self, rating):
    self.score += rating
    self.votes += 1

  def __str__(self):
    return self.name+'('+str(self.pk)+')'

# A Genre of games, a way to categorize different games 
class Genre(models.Model):
  name = models.CharField(max_length=50)
  games = models.ManyToManyField('Game',through=Game.genres.through,blank=True, null=True)

  class Meta:
    db_table = 'Genres'
    managed = True
    ordering = ['name']
    verbose_name = 'genre'
    verbose_name_plural = 'genres'
    
  def __str__(self):
    return self.name

# A review of a game with a rating for itself and for the game
class Review(models.Model):
  title = models.CharField(max_length=50)
  content = models.TextField("Text of the review",max_length=20000)
  autor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
  of = models.OneToOneField('Game', on_delete=models.DO_NOTHING)
  game_rating = models.DecimalField("Review rating of the game from 1 to 10", max_digits=3, decimal_places=1, default=0)
  score = models.DecimalField("rating of the raview from 1 to 10", max_digits=3, decimal_places=1, default=0)
  votes = models.IntegerField("number of times this review has been voted (used to calculate review_rating)", default=0)

  class Meta:
    db_table = 'Reviews'
    managed = True
    ordering = ['autor']
    verbose_name = 'review'
    verbose_name_plural = 'reviews'

  def get_rating(self):
    return self.score/self.votes

  def rate(self, rating):
    self.score += rating
    self.votes += 1

  def __str__(self):
    return self.title+' ['+self.game_rating+']'
