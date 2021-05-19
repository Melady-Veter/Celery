from django.shortcuts import render
from .tasks import text


# Create your views here.
def index(request):
    text.delay()
    return render(request, 'index.html')
