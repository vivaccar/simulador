
from typing import Any
from django.core.management import BaseCommand
from ...models import Game, League, Team
from math import modf
from ...scripts import restart_teams, check_stadiums, convert_date, get_updated_games, aproveitamento, update_table

class Command(BaseCommand):
	def handle(self, *args, **options):
		get_updated_games(71, 2024)
		get_updated_games(72, 2024)
		get_updated_games(39, 2023)
		get_updated_games(140, 2023)
		get_updated_games(78, 2023)
		get_updated_games(135, 2023)
		get_updated_games(94, 2023)
		games = Game.objects.all()
		check_stadiums(games)
		self.stdout.write(self.style.SUCCESS('UPDATED DATA'))
	