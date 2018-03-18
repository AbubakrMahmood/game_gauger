from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage': "this is the bold text from views.py"}
    return render(request, 'review/index.html', context=context_dict)

def about(request):
    return render(request, 'review/about.html')
