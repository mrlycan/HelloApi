from django.db import models
import  time

class Team(models.Model):
	TeamId=models.IntegerField()
	TeamENName=models.CharField(max_length=100)
	TeamCNName=models.CharField(max_length=100)
	LeagueId=models.IntegerField()
	LeagueName=models.CharField(max_length=100)
	CourtName=models.CharField(max_length=100)
	FoundingTime=models.DateTimeField()
	TeamLogoImage=models.CharField(max_length=100)
	CourtImage=models.CharField(max_length=100)
	Remark=models.TextField()
	UpdateTime=models.DateTimeField(default=time.time())
	class Meta:
		ordering=('TeamId',)

class Season(models.Model):
	SeasonId = models.IntegerField()
	SeasonName = models.CharField(max_length=100)
	LeagueId = models.IntegerField()
	LeagueName = models.CharField(max_length=100)
	IsHistory = models.BooleanField(default=False)
	BeginTime = models.DateTimeField()
	EndTime = models.DateTimeField()
	class Meta:
		ordering=('SeasonId',)

class Player(models.Model):
	CNName = models.CharField(max_length=100)
	ENName = models.CharField(max_length=100)
	TeamId = models.IntegerField()
	TeamName = models.CharField(max_length=100)
	Number = models.DateTimeField()
	ImageUrl = models.CharField(max_length=100)
	class Meta:
		ordering=('TeamId',)

class Country(models.Model):
	CountryId = models.IntegerField()
	CountryName = models.CharField(max_length=100)
	CountryENName = models.CharField(max_length=100)
	Image = models.CharField(max_length=100)
	InternalName = models.CharField(max_length=100)
	Code = models.DateTimeField()

	class Meta:
		ordering=('CountryId',)

class League(models.Model):
	LeagueId = models.IntegerField()
	LeagueName = models.CharField(max_length=100)
	ENName = models.CharField(max_length=100)
	CountryId = models.IntegerField()
	CountryName = models.CharField(max_length=100)
	Levels = models.IntegerField()
	TeamCount = models.IntegerField()
	InternalName = models.CharField(max_length=100)
	EventType = models.IntegerField()
	ImageUrl = models.CharField(max_length=100)
	Remark = models.TextField()
	class Meta:
		ordering=('LeagueId',)

