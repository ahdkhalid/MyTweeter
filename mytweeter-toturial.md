# Mytweeter toturial -cheatsheet

# Setup the environment 
```
cd ../pr_projects/      # project base
python3 -m pip install pipenv --upgrade
mkdir mytweeter         #create project folder
cd mytweeter
pipenv install --python 3 django==2.2 ##create virtual env and install django
```
## activate virtual env
```
pipenv shell
ls
```
## create the project
```
django-admin startproject mytweeter .
```
## Enabling Git
```
git init
git add .
git commit -m 'init project'
```
## changing some VS Code settings
In the settings, search for python, edit python path to python3.

## Starting the development 
Writing a roadmap is helpful so you can do that. 
We start by creating the tweets app.
```
python manage.py startapp tweets
```
Adding it to settings.py under 'INSTALLED_APPS', then:
```
class Tweet(models.Model):
    # id        = models.AutoField(primary_key = True)
    content     = models.TextField (blank = True, null =True) # blank for django, null for db
    image     = models.FileField (blank = True, null =True)
```
We can test out our model object and even write to them from the shell.
```
python manage.py shell
```
and under shell:
```
from tweets.models import Tweet
obj = Tweet()
obj.abc = 23    #new attribute
obj.save()      # but won't be save to db as it only looks in django model class
obj.content ='hello world'  # this can be saved as it's attr of model
## or create using create function:
obj=Tweet.objects.create(content ="Hello 2")

content-on-db = obj.objects.get(content)
print (content-on-db)

```

# URL routing and dynamic routing 
Defualt view of a newly created django project is a static page by django.\ 
To create our first view, we edit tweets app views.py 
```
def home_view(request, *args, **kwarg):
    return HttpResponse('<h1>Hello World<h1>')
```
and add the url to main urls.py
```
from tweets.views import home_view
urlpatterns = [
  path('', home_view),
  path('abc/', home_view),
    path('tweets/<int:tweet_id>', home_view),
```
Note that we can have any other and even dynamic urls pointing to a single view\
but let's create a seprate view for tweet detail. in views.py
```
def tweet_detail_view(request,tweet_id, *args, **kwarg):
    return HttpResponse(f'<h1> Hello {tweet_id} <h1>')
```
also updating urls.py
```
path('tweets/<int:tweet_id>', tweet_detail_view),
```
Dynamic URL with is own view. that tweet_id is taken from **kwargs argument of the function. \
Now, let's make kinda real tweet details view. and get data from db
```
def tweet_detail_view(request,tweet_id, *args, **kwarg):
    try:
        obj     = Tweet.objects.get(id = tweet_id)
    except:
        raise Http404 #import it
    return HttpResponse(f'<h1> Hello {tweet_id} content: {obj.content}<h1>')
```
## creating our REST API view
We need the api to connect to javascript/java/swift and other langueges. \
So the base thing in having our api: 
```
def tweet_detail_view(request,tweet_id, *args, **kwarg):
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
        return JsonResponse(data, status= status) #import it
    return JsonResponse(data, status)
```
## tweet list api view
Writing the view and adding it to urls.py
```
def tweet_list_view(request, *args, **kwarg):
    '''
    REST API VIEW
    For Javascript/React
    '''
    qs  = Tweet.objects.all()
    tweets_list =[{'id': x.id, 'content': x.content} for x in qs]
    data ={
        'response': tweets_list
    }
    return JsonResponse(data)
```

## Dynamic Load Tweets via JavaScript
All to do now is to edit home.html and test out and get data from /tweets endpoint using javascript.
```
<script>
    const xhr = new XMLHttpRequest()
    const method = "GET"
    const url   = "/tweets"
    const responseType = "json"

    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.onload = function(){
        const serverResponse = xhr.response
        var listedItems = serverResponse.response  
        console.log(listedItems)
    }
    xhr.send()
</script>
{% endblock content %}
```
Testing it out will be using *inspect element* under console of the browser \
## load tweets with javascript
first we neeed to specify the place the tweets should be displayed. in the home.html we define the dev to contain the tweets
<div id="tweets">
    Loading!
</div>
then we use javascrip to load them separately and display them.


```
    const tweetsElement =document.getElementById("tweets") // defined at the top- pointing to <dev> of tweets
        const listedItems = serverResponse.response  
        
        var finalTweetStr = ""
        var i;
        for (i=0; i<listedItems.length; i++){
            console.log(i)
            console.log(listedItems[i])
            var currentItem = "<div class='mb-4'><h1>" + listedItems[i].id +"</h1>" +"<p>"+ listedItems[i].content + "</p></dev>"
            finalTweetStr += currentItem
        }
        tweetsElement.innerHTML = finalTweetStr //replaces the content of html element
 
    }
```
## formating the tweet 
It much cleaner to have the funtion to have the format of tweet and bring change in single place in future. And better to remove h1 and add tweet id as id of div element and add extra class too. so under the same script tag and under const initializations, 
```

    function formatTweetElement (tweet){
        var formatTweet = "<div class='mb-4 tweet' id='tweet-" + tweet.id +">'<p>"+ tweet.content + "</p></dev>"
        return formatTweet
    }
```
And inside for loop (from above), we delete the console logs too.
```
        for (i=0; i<listedItems.length; i++){
            var tweetObject = listedItems[i]
            var currentItem = formatTweetElement(tweetObject)
            finalTweetStr += currentItem
        }
```
## like button rendering
For now a sample like button is created with bootstrap styles and a simple action on it (logging in console) while clicking. Other changes to formatTweetElement also made:
```
function handleDidLike (tweet_id, currentCount) {
    console.log(tweet_id, currentCount)
    return 
}

function LikeBtn(tweet) {
    return "<button class='btn btn-primary btn-sm' onclick=handleDidLike(" + 
    tweet.id + "," + tweet.likes + ")>" + tweet.likes + " Likes</button>"
}

function formatTweetElement(tweet) {
    var formattedTweet = "<div class='mb-4 tweet' id='tweet-" + tweet.id 
    + "'><p>" + tweet.content + 
        "</p><div class='btn-group'>" + LikeBtn(tweet) +
        "</div></div>"
    return formattedTweet
}
```
We also have to edit views.py to add *likes* data (we do it randomly for now)
```
    tweets_list =[{'id': x.id, 'content': x.content, 'likes':random.randint(0,200)} for x in qs]

```
But,\
To make this like click funtional to the app lots of javascript code needs to be written and will overwhelms the project thus not very practical and very time consuming. So here JavaScript shows is limitations. 

# Rapid implement of Bootstrap theme
Bootstrap is one the most used templates treasure/provider and widely used. 
Go to getbootstrap.com and get themes you want and other compannents. for now we want some navbar and footer component and we get its simple /defualt style from the site. 
So we create components folder and footer.html and navbar.html inside. then copy pasting one navbar from bootstrip into into components/navbar.html. Then bringin any change we wish too. Like applying *d-none* class to some page links in the navbar which are not yet active. and so on. Not going put the code for navbar.html\
Then bringig some changes to base.html to include the navbar
```
    <style>
      .bg-tweetme {
          background-color: #8e1f1f!important;
      }
    </style>
    <title>MyTweeter {% block head_title %} {% endblock head_title %}</title>
  </head>
  <body>
    {% include "components/navbar.html" %}
    <div class='container'>
      {% block content %}
      {% endblock content %}
    </div>
```
And also changing home.html and updating the look of the tweet list (e.g create border) and containerzing all tweets and anything to make it look good. but don't put too much time.
Changes at home.html are (different parts):
```
<div class='row text-center'>
    <div class='col'>
        <h1>Welcome to Mytweeter</h1>
    </div>
</div>

<div class="row" id="tweets">
    Loading!
</div>

        var formattedTweet = "<div class='col-12 col-md-10 mx-auto border rounded py-3 mb-4 tweet' id='tweet-" + tweet.id 

```
