from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import is_safe_url
from django.conf import settings
import random

from .models import Tweet
from .forms import TweetForm

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_view(request, *args, **kwarg):
    return render(request,'pages/home.html',context ={}, status=200)

def tweet_create_view(request, *args, **kwargs):
    user    = request.user
    print (user)
    if not user.is_authenticated:
        user = None
        if request.is_ajax():
            return JsonResponse({},status= 401)
        return redirect(settings.LOGIN_URL)
    form = TweetForm(request.POST or None)
    next_url = request.POST.get('next')
    if form.is_valid():
        obj = form.save(commit=False)
        # do other form related logic
        obj.user = user
        obj.save()
        if request.is_ajax():
            print ('Ajax enabled')
            return JsonResponse(obj.serialize(), status= 201) # item created 
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status =400)
    return render(request, 'components/form.html', context={"form": form})

def tweet_list_view(request, *args, **kwarg):
    '''
    REST API VIEW
    For Javascript/React
    '''
    qs  = Tweet.objects.all()
    tweets_list =[x.serialize() for x in qs]
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
