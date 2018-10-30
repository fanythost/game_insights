from django.db import models

# Game data with it's respective information
class Game(models.Model):
  name = models.CharField("The name of the game", max_length=50)
  franchise = models.CharField("The franchise of the game", max_length=50)
  publisher = models.CharField("The Publisher of the game", max_length=50) # TODO publisher must be a model with games list
  rating = models.DecimalField("User rating of the game from 1 to 10", max_digits=3, decimal_places=1)
  genres = models.ManyToManyField('Genre',blank=True)
  overview = models.TextField("Quick description of the game",max_length=400)

  
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

  





