from django.contrib import admin
from .models import Player, Border, Capital, Game
# Register your models here.


class PlayerAdmin(admin.ModelAdmin):
    fields = ['player_name', 'user']
    list_display = ('player_name',)

class BorderAdmin(admin.ModelAdmin):
    fields = ['x', 'y', 'border_name']
    list_display = ('x', 'y', 'border_name')

class CapitalAdmin(admin.ModelAdmin):
    fields = ['capital_name', 'borders', 'ruler']
    list_display = ('capital_name',)

class GameAdmin(admin.ModelAdmin):
    fields = ['game_ready', 'game_players']
    list_display = ()


admin.site.register(Player, PlayerAdmin)
admin.site.register(Border, BorderAdmin)
admin.site.register(Capital, CapitalAdmin)
admin.site.register(Game, GameAdmin)
