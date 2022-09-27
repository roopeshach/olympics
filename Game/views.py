from django.shortcuts import render, redirect
from .models import Game, MatchPlayer, MatchSummary, Player , Match, Stream, Comment, News
# Create your views here.
from django.http import  JsonResponse

def index(request):
    games = Game.objects.all()[:4]
    players = Player.objects.all()
    matches = Match.objects.all()[:4]
    summaries = MatchSummary.objects.all()
    streams = Stream.objects.all()[:8]
    context = {
        'games': games,
        'players': players,
        'matches': matches,
        'summaries': summaries,
        'streams': streams


    }
    return render(request, 'Game/index.html', context)

def game(request):
    games = Game.objects.all()
    return render(request, 'Game/game.html', {'games': games})

def player(request):
    players = Player.objects.all()
    return render(request, 'Game/player.html', {'players': players})

def match(request):
    matches = Match.objects.all()
    return render(request, 'Game/match.html', {'matches': matches})

def match_summary(request):
    summaries = MatchSummary.objects.all()
    context = {
        'summaries': summaries
    }
    return render(request, 'Game/match_summary.html', context)

def stream(request):
    streams = Stream.objects.all()
    context = {
        'streams': streams
    }

    return render(request, 'Game/stream.html', context)

def stream_page(request, id):
    stream = Stream.objects.get(id=id)
    comments = Comment.objects.filter(stream = stream)
    context = {
        'stream': stream,
        'comments': comments
    }
    return render(request, 'Game/stream_page.html', context)

def add_visit(request, id):
    stream = Stream.objects.get(id=id)
    stream.visits += 1
    stream.save()
    return redirect(request.META.get('HTTP_REFERER'))


def add_comment(request):
    if request.method == 'POST':
        stream_id = request.POST.get('stream_id')
        stream = Stream.objects.get(id=stream_id)
        comment = request.POST.get('comment')
        user = request.user
        comment = Comment(
            stream = stream,
            user = user,
            text = comment
        )
        comment.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'failed'})




def player_profile(request, id):
    player = Player.objects.get(id=id)
    context = {
        'player': player,

    }
    return render(request, 'Game/player_profile.html', context)

def match_detail(request, id):
    match = Match.objects.get(id=id)
    players = MatchPlayer.objects.filter(match = match)
    context = {
        'match':match,
        'players':players
    }
    return render(request , 'Game/match_details.html', context)


def news(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'Game/news.html', context)

def news_detail(request, id):
    news = News.objects.get(id=id)
    context = {
        'news': news
    }
    return render(request, 'Game/news_detail.html', context)
