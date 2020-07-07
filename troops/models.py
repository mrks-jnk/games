from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.



class Player(models.Model):
    #ki = models.BooleanField(default=True)
    player_name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.player_name


class Border(models.Model):
    border_name = models.CharField(max_length=20, default='border')
    x = models.IntegerField()
    y = models.IntegerField()

    def __str__(self):
        return 'x: {}, y: {}'.format(self.x, self.y)


class Capital(models.Model):
    capital_name = models.CharField(max_length=20)
    borders = models.ManyToManyField(Border)
    ruler = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return self.capital_name


class Game(models.Model):
    game_ready = models.BooleanField(default=False)
    game_players = models.ManyToManyField(Player)
