# How To Create a Hello World App in Django

## Step 1: Create a Virtual Environment
First we will need to create a virtual environment to make sure we are all on the same page.

Let's install django.

`pip install django`

## Step 2: Create the Directory Structure
Let's get our directory structure set up.

```bash
mkdir my_django_project
cd my_django_project
django-admin startproject helloworld_project
```
## Step 3: Try to Run Our Project

Let's cd into our outer project directory and try to run the app.
```bash
cd helloworld_project
python manage.py runserver
```

It will tell us, we have 13 unapplied migrations. Now let's run a migration.

`python manage.py migrate`

## Step 4: Try to Run Our Project Again
Let's try this again:
`python manage.py runserver`

And now we can visit localhost:8000 and see what we have.

## Step 5: Let's Create an App
Now we can create an app inside of our project.
`django-admin startapp my_app`

## Step 6: Let's Update Our Settings
In settings.py let's update our settings under installed apps to include our app.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_app',
]
```

## Step 7: Let's Set Up for Templates
In our console let's set up the framework to create a template for our basic app to use.

```bash
cd my_app
mkdir templates
cd templates
touch index.html
```

## Step 8: Let's Edit Our Index File

Inside index.html let's add the following code.

```html
<html>
<head><title>Home Page</title></head>
<body>
Hello world
</body>
</html>
```

## Step 9: Setting Up Our Views

Now let's add the following to the generic boiler plate django creates for us.

```python
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'
```

## Step 10: Updating URLs
Now we need to go into urls.py and make sure we can have everything all set up.

```python
from django.conf.urls import url
from django.contrib import admin
from my_app.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
]
```

## Step 11: Now we Can Run It!
Now we can go in and run our simple django site.

```bash
cd ..
python manage.py runserver
```
