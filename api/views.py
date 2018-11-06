from rest_framework import viewsets, generics
from api.serializers import UserSerializer, GroupSerializer, GameSerializer, GenreSerializer, ReviewSerializer
from api.models import Game, Genre, Review


class GameViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows games to be viewed or edited.
  """
  queryset = Game.objects.all()
  serializer_class = GameSerializer

class GenreViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows genres to be viewed or edited.
  """
  queryset = Genre.objects.all()
  serializer_class = GenreSerializer

class ReviewViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows genres to be viewed or edited.
  """
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer

