from django.shortcuts import render
from rest_framework import viewsets, mixins
from .serializers import PollSerializer
from rest_framework.decorators import detail_route
from .models import Poll, Choice
from rest_framework.response import Response

def create(request):
	return render(request, 'PollApp/createpoll.html')

def vote(request, poll_id):
	return render(request, 'PollApp/votepoll.html')

class PollViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	queryset = Poll.objects.all()
	serializer_class = PollSerializer

	@detail_route(methods=['post'])
	def vote_choice(self, request, pk=None):
		selected_choices = request.query_params.get('selectedChoices')

		choices = Choice.objects.filter(
			id__in = selected_choices
			).filter(
			poll_id = pk
			)

		if not choices:
			return Response({ 'status' : 'failure' })

		for choice in choices: 
			choice.votes += 1
			choice.save()

		return Response({ 'status' : 'success'})