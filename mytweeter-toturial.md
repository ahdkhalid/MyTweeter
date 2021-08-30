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
