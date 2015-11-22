from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PollSerializer
from .models import Poll

# Create your views here.
def create(request):
	return render(request, 'PollApp/createpoll.html')

	# Create your views here.
def vote(request):
	return render(request, 'PollApp/votepoll.html')

class PollViewSet(viewsets.ModelViewSet):
	queryset = Poll.objects.all()
	serializer_class = PollSerializer