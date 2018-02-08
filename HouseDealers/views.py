from django.shortcuts import render
from django.utils import timezone
from .models import Ngome

# Create your views here.
#from django.http import HttpResponse


#def index(request):
#   return HttpResponse("Khamis Hussein")
	
def post_list(request):
	ngomes = Ngome.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'HouseDealers/post_list.html', {'ngomes': ngomes})