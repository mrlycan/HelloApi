from rest_framework import serializers
import Hello.models as models

class SeasonSerializer(serializers.ModelSerializer):
	class Mate:
		model=models.league_season
		fields=('id','SeasonId','SeasonName','LeagueId','LeagueName','IsHistory','BeginTime','EndTime')