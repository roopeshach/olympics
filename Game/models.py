from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    expertise = models.CharField(max_length=100)
    medals_won = models.CharField(max_length=4, blank=True, default=0)
    image = models.ImageField(upload_to='players')

    def __str__(self):
        return self.name + ' - ' + self.country
    
    def get_absolute_url(self):
        return reverse('Game:player-profile', args=[str(self.id)])

class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='games')

    def __str__(self):
        return self.name
    
    def get_matches(self):
        return self.match_set.all()
        

class Match(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    stadium = models.CharField(max_length=100)

    image = models.ImageField(upload_to='matches', blank=True, null=True)

    def __str__(self):
        return self.game.name + ' - ' + str(self.date)

class MatchPlayer(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.player.name + ' - ' + str(self.score)


class MatchSummary(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    gold_winner = models.CharField(max_length=250)
    silver_winner = models.CharField(max_length=250)
    bronze_winner = models.CharField(max_length=250)

    description = models.TextField()

    def __str__(self):
        return self.match.game.name + ' - ' + str(self.match.date)



class Stream(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='streams', blank=True, null=True)
    description = models.TextField()
    video = models.FileField(upload_to='stream_videos', blank=True, null=True)
    visits = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('Game:stream', args=[str(self.id)])
    
    def update_visits(self):
        self.visits += 1
        self.save()

class Comment(models.Model):
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User',  on_delete=models.CASCADE)
    text = models.CharField(max_length=254)
    
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stream.name 

    
class News(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news')
    description = models.TextField()

    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Game:news-detail', args=[str(self.id)])



