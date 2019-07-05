from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home0(request):
	return render(request, 'drink/home.html')

@login_required
def home(request):
    return render(request, 'drink/1.html')