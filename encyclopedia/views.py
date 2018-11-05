from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from api.models import Game, Genre
import json
# Create your views here.



# home view
class Home(View):
    
    def get(self, request):
        api = "http://localhost:8000/api/genres/"
        games = Game.objects.all()
        genres = Genre.objects.all()
        filter_genres = []
        data = {'games':games, 'genres':genres, 'filter_genres':filter_genres, 'api':api}
        
        return render(request, 'home.html', data)
    
    def post(self, request):
        api = "http://localhost:8000/api/genres/"
        if request.POST.get('genres'):
            pks = request.GET.get('genres', None)
            games = Game.objects.filter(genres__in=pks)
            genres = Genre.objects.all()
            filter_genres = Genre.objects.filter(pk__in=pks)
            data = {'games':games, 'genres':genres, 'filter_genres':filter_genres, 'api':api}

            return render(request, 'home.html', data)


