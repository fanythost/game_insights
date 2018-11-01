from django.shortcuts import render
from django.views import View
from api.models import Game, Genre
# Create your views here.

# home view
class Home(View):
    def get(self, request):
        games = Game.objects.all()
        genres = Genre.objects.all()
        data = {
            'games': games,
            'genres': genres
        }
        return render(request, 'home.html', data)

