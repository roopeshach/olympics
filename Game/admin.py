from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import Player, Game, Match, MatchPlayer, Stream, MatchSummary, News

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'age', 'expertise','medals_won', 'image_tag')
    list_filter = ('country', 'age', 'expertise','medals_won')
    search_fields = ('name', 'country', 'age', 'expertise','medals_won')

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 150px; height:150px;" />'.format(obj.image.url))
    
    image_tag.short_description = 'Image'


class GameAdmin(admin.ModelAdmin):
    #show players in game
    list_display = ('name','description',  'image_tag')
    list_filter = ('name',)
    search_fields = ('name',)
    
    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 150px; height:150px;" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

class MatchPlayerTabularInline(admin.TabularInline):
    model = MatchPlayer
    extra = 4


class MatchAdmin(admin.ModelAdmin):
    list_display = ('game', 'date', 'time', 'description', 'image_tag', 'stadium', 'match_players')
    list_filter = ('game', 'date', 'time')
    search_fields = ('game', 'date', 'time')
    inlines = [MatchPlayerTabularInline]
    
    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 150px; height:150px;" />'.format(obj.image.url))


    def match_players(self, obj):
        return ", ".join([p.player.name for p in obj.matchplayer_set.all()])
    


    image_tag.short_description = 'Image'



class StreamAdmin(admin.ModelAdmin):
    list_display = ('match', 'name',  'description', 'image_tag', 'visits')
    list_filter = ('match', 'name')
    search_fields = ('match', 'name')

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 150px; height:150px;" />'.format(obj.image.url))
    
    image_tag.short_description = 'Image'
    
class MatchSummaryAdmin(admin.ModelAdmin):
    list_display = ('match', 'gold_winner', 'silver_winner', 'bronze_winner', 'description')
    list_filter = ('match',)
    search_fields = ('match',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_tag')
    list_filter = ('title',)
    search_fields = ('title',)

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 150px; height:150px;" />'.format(obj.image.url))
    
    image_tag.short_description = 'Image'



admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Stream, StreamAdmin)
admin.site.register(MatchSummary, MatchSummaryAdmin)
admin.site.register(News, NewsAdmin)

