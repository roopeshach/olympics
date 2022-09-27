from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game', views.game, name='game'),
    path('player', views.player, name='player'),
    path('match-summary', views.match_summary, name='match-summary'),
    path('match', views.match, name='match'),
    path('player-profile/<int:id>', views.player_profile, name='player-profile'),
    path('match-detail/<int:id>', views.match_detail, name="match-detail"),
    path('stream', views.stream, name='stream'),
    path('stream-page/<int:id>', views.stream_page, name='stream-page'),
    path('add-comment', views.add_comment, name='add-comment'),
    path('add-visit/<int:id>', views.add_visit, name='add-visit'),

    path('news', views.news, name='news'),
    path('news-detail/<int:id>', views.news_detail, name='news-detail'),
]
