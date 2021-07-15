from django.shortcuts import render
def index(request):
    return render(request, 'food/index.html')
# Create your views here.
