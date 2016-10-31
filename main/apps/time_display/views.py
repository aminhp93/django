from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.
def index(request):
	time = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
	print(time)
	return render(request, 'index.html', {"time": time})
	