from django.db import models
from .fight import Fight
from .clan_user import ClanUser
from .discord_server import DiscordServer

class FightParticipation(models.Model):
    fight=models.ForeignKey(Fight)
    user=models.ForeignKey(ClanUser)
    guild=models.ForeignKey(DiscordServer)

    def __str__(self):
        return self.fight.__str__()