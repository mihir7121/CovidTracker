from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # context = {'latest_question_list': latest_question_list}
    context = {}
    return render(request, 'app/index.html', context)