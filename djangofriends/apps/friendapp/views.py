from django.shortcuts import render
from . import models
# Create your views here.
def index(req):
    # users = models.Users.objects.all()
    # users = models.Users.objects.filter(id__lte=7)
    # users = models.Users.objects.filter(last_name="Rodriguez")
    # users = models.Users.objects.all().order_by('last_name', 'first_name')
    # users = models.Users.objects.filter(id=4) | models.Users.objects.filter(id=5)
    # users = models.Friendships.objects.filter(user__id = 2)
    # users = models.Friendships.objects.filter(user__first_name = "Michael")
    # users = models.Friendships.objects.all()
    users = models.Friendships.objects.filter(user__id = 1 && user__last_name = "Hernandez") 
    context = {'users':users}
    return render(req, "friendapp/index.html",context)
