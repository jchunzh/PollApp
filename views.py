from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PollSerializer
from rest_framework.decorators import detail_route
from .models import Poll, Choice
from rest_framework.response import Response
import pprint

def create(request):
	return render(request, 'PollApp/createpoll.html')

def vote(request):
	return render(request, 'PollApp/votepoll.html')

class PollViewSet(viewsets.ModelViewSet):
	queryset = Poll.objects.all()
	serializer_class = PollSerializer

	@detail_route(methods=['post'])
	def vote_choice(self, request, pk=None):
		print("vote")

		choice_id = request.query_params.get('choiceId')

		print(choice_id)
		print(pk)

		choices = Choice.objects.filter(
			id = choice_id
			).filter(
			poll_id = pk
			)



		if not choices:
			pass
		else:
			choice = choices[0]
			print(choice)
			print(choice.id)
			print(choice.text)
			print(choice.votes)
			choice.votes += 1
			choice.save()

		return Response({ 'status' : 'success'})