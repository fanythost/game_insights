from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Game, Genre, Review


class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ('url', 'name')

class GameSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Game
    fields = ('__all__')

class GenreSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Genre
    fields = ('__all__')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    
    model = Review
    fields = ('of','title','content','game_rating','score','votes')    