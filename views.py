from django.shortcuts import render
from rest_framework import viewsets, mixins
from .serializers import PollSerializer
from rest_framework.decorators import detail_route
from .models import Poll, Choice
from rest_framework.response import Response
from PollApp.Repositories.PollRepository import PollRepository
from PollApp.Repositories.ChoiceRepository import ChoiceRepository
from PollApp.Facades.PollFacade import PollFacade

def create(request):
	return render(request, 'PollApp/createpoll.html')

def vote(request):
	return render(request, 'PollApp/votepoll.html')

def results(request):
	return render(request, 'PollApp/pollresults.html')

class PollViewSet(viewsets.ViewSet):
	queryset = Poll.objects.all()
	serializer_class = PollSerializer
	
	def create(self, request, pk=None):
		pollData = request.data
		
		choicesData = request.data.pop('choices')
		poll = Poll(**pollData)
		choices = []
		
		for choice in choicesData:
			choices.append(Choice(**choice))

		PollFacade().create(poll, choices)
		
		serializer = PollSerializer(poll)
		return Response({ 'poll' : serializer.data })
	
	def retrieve(self, request, pk=None):
		poll = PollRepository().getPollByUniqueId(pk)
		serializer = PollSerializer(poll)

		return Response({ 'poll' : serializer.data })

	@detail_route(methods=['post'])
	def vote_choice(self, request, pk=None):
		selected_choices = request.query_params.getlist('selectedChoices')
		
		ChoiceRepository().voteForChoices(selected_choices)

		return Response({ 'status' : 'success'})