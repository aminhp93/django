from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, "index.html")

def show(request):
	print(request.method)
	return render(request, "show.html")

def create(request):
	print(request.method)
	if request.method == "POST":
		print("*" * 40)
		print(request.POST)
		request.session['name'] = request.POST['name']
		print(request.session)
		print('name' in request.session)
		return render(request, "new.html")
	else:
		return redirect('/')