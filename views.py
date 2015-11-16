from django.shortcuts import render

# Create your views here.
def create(request):
	return render(request, 'PollApp/createpoll.html')

	# Create your views here.
def vote(request):
	return render(request, 'PollApp/votepoll.html')