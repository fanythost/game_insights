from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, GameSerializer, GenreSerializer
from api.models import Game, Genre


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

