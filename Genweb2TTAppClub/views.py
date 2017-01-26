from django.shortcuts import render

from django.views import generic
from models import Match
from django.utils import timezone
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'Genweb2TTAppClub/index.html'
    context_object_name = 'match_list'

    def get_queryset(self):
        return Match.objects.all()

    '''def index(request):
       return HttpResponse("Welcome to Genweb2 TT Club!")'''

class DetailView(generic.DetailView):
    model = Match
    template_name = 'Genweb2TTAppClub/detail.html'

    def get_queryset(self):
        return Match.objects.filter(MatchDate=timezone.now())
        #return Match.objects.all()