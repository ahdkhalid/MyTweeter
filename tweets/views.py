from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
import random

from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwarg):
    return render(request,'pages/home.html',context ={}, status=200)

def tweet_list_view(request, *args, **kwarg):
    '''
    REST API VIEW
    For Javascript/React
    '''
    qs  = Tweet.objects.all()
    tweets_list =[{'id': x.id, 'content': x.content, 'likes':random.randint(0,200)} for x in qs]
    data ={
        'response': tweets_list
    }
    return JsonResponse(data)
def tweet_detail_view(request,tweet_id, *args, **kwarg):
    '''
    REST API VIEW
    For Javascript/React
    '''
    data = {
        'id': tweet_id,
    }
    status = 200
    try:
        obj     = Tweet.objects.get(id= tweet_id)
        data['content'] = obj.content
    except:
        status = 404
        data['message'] = 'Not Found'
        return JsonResponse(data, status= status)
    return JsonResponse(data, status)
