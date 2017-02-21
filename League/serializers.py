from rest_framework import serializers
import League.models as models

class Team(serializers.ModelSerializer):
	class Meta:
		model=models.Team
		fields=(
				'id',
				'TeamId',
				'TeamENName',
				'TeamCNName',
				'LeagueId',
				'LeagueName',
				'CourtName',
				'FoundingTime',
				'TeamLogoImage',
				'CourtImage',
				'Remark',
				'UpdateTime')


class Season(serializers.ModelSerializer):
	class Meta:
		model=models.Season
		fields=(
			'id',
			'SeasonId',
			'SeasonName',
			'LeagueId',
			'LeagueName',
			'IsHistory',
			'BeginTime',
			'EndTime'
		)

class Player(serializers.ModelSerializer):
	class Meta:
		model=models.Player
		fields=(
			'id',
			'CNName',
			'ENName',
			'TeamId',
			'TeamName',
			'Number',
			'ImageUrl'
		)

class Country(serializers.ModelSerializer):
	class Meta:
		model=models.Country
		fields=(
			'id',
			'CountryId',
			'CountryName',
			'CountryENName',
			'Image',
			'InternalName',
			'Code'
		)

class League(serializers.ModelSerializer):
	class Meta:
		model=models.League
		fields=(
			'id',
			'LeagueId',
			'LeagueName',
			'ENName',
			'CountryId',
			'CountryName',
			'Levels',
			'TeamCount',
			'InternalName',
			'EventType',
			'ImageUrl',
			'Remark'
		)