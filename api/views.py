from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, GameSerializer, GenreSerializer
from api.models import Game, Genre


class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Group.objects.all()
  serializer_class = GroupSerializer


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

