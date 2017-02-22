from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import football.models.models as models
import football.serializers as serializers


class JSONResponse(HttpResponse):
	"""
	 An HttpResponse that renders its content into JSON.
	"""

	def __init__(self,data,**kwargs):
		content=JSONRenderer().render(data)
		kwargs['content_type']='application/json'
		super(JSONResponse, self).__init__(content,**kwargs)

@csrf_exempt
def team_list(request):
	"""
	List all code snippets, or create a new snippet.
	"""
	if request.method == 'GET':
		Teams = models.Team.objects.all()
		serializer = serializers.Team(Teams, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = serializers.Team(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def team_detail(request, pk):

	try:
		Team = models.Team.objects.get(pk=pk)
	except Team.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = serializers.Team(Team)
		return JSONResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = serializers.Team(Team, data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data)
		return JSONResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		Team.delete()
		return HttpResponse(status=204)
