from django.shortcuts import render
import random
import string

# Create your views here.
def index(request):
	if ('number' not in request.session):
		request.session['number'] = 0
	request.session['number'] += 1
	request.session['name'] = "MINH"
	n = 16
	result = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

	return render(request, "index.html", {'result': result, 'name': request.session['name'], 'number': request.session['number']})