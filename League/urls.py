from django.conf.urls import url
from League import views

urlpatterns =[
	url(r'^league/team/$', views.team_list),
	url(r'^league/team/(?P<pk>[0-9]+)/$', views.team_detail)
 ]