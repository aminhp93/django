from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')

def show(request):
	if (not 'number' in request.session):
		request.session['number'] = 1
	request.session['number'] += 1
	name = request.POST['name']
	return render(request, 'show.html', {'name': name})