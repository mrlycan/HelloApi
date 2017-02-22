from django.conf.urls import url
#from football import views
import football.views as views

urlpatterns =[
	url(r'^football/team/$', views.team.team_list),
	url(r'^football/team/(?P<pk>[0-9]+)/$', views.team.team_detail)
 ]