from django.shortcuts import render, redirect
from .models import Message, Comment

# Create your views here.
def index(request):
	messages = Message.objects.all()
	comments = Comment.objects.all()
	return render(request, 'index.html', {'messages': messages, 'comments': comments})

def create_message(request):
	Message.objects.create(message=request.POST['message'])
	return redirect('/')

def create_comment(request, id):
	message = Message.objects.get(id=id)
	Comment.objects.create(comment=request.POST['comment'], message_id = message)
	return redirect('/')
