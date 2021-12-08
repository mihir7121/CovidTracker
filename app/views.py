from django.shortcuts import render
from django.http import HttpResponse
import requests
import time
import json
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
def index(request):
    # context = {'latest_question_list': latest_question_list}
    attempt_num = 0
    res = requests.get("http://localhost:3000/AN", timeout=10)
    if res.status_code == 200:
        data = json.loads(res.text)
        data = json.dumps(data)
        print(data)
    else:
        attempt_num += 1
        time.sleep(5)
    context = {data: data}
    return render(request, 'app/index.html', context)