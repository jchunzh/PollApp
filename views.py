from django.shortcuts import render
from rest_framework import viewsets, mixins
from .serializers import PollSerializer
from rest_framework.decorators import detail_route
from .models import Poll, Choice
from rest_framework.response import Response
from PollApp.Repositories.PollRepository import PollRepository
from PollApp.Repositories.ChoiceRepository import ChoiceRepository

def create(request):
	return render(request, 'PollApp/createpoll.html')

def vote(request):
	return render(request, 'PollApp/votepoll.html')

def results(request):
	return render(request, 'PollApp/pollresults.html')

class PollViewSet(viewsets.ViewSet):
	queryset = Poll.objects.all()
	serializer_class = PollSerializer
	_pollRepository = PollRepository();
	_choiceRepository = ChoiceRepository()
	
	def create(self, request, pk=None):
		pollData = request.data
		
		choicesData = request.data.pop('choices')
		poll = self._pollRepository.createPoll(pollData)
		
		for choice in choicesData:
			self._choiceRepository.create(poll, **choice)
		
		serializer = PollSerializer(poll)
		return Response({ 'poll' : serializer.data })
	
	def retrieve(self, request, pk=None):
		repo = PollRepository()
		poll = repo.getPollByUniqueId(pk)
		serializer = PollSerializer(poll)
		return Response({ 'poll' : serializer.data })

	@detail_route(methods=['post'])
	def vote_choice(self, request, pk=None):
		selected_choices = request.query_params.getlist('selectedChoices')
		
		print(selected_choices);

		self._choiceRepository.voteForChoices(selected_choices)

		return Response({ 'status' : 'success'})