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
