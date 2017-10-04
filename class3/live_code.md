# Flask Code Demo 

# Create a Virtual Environment
I suggest using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

# Install Flask
`pip install Flask`

# Let's do a pip freeze to see what happens

We see these packages get installed for you.

- Click (Command Line Interface Creation Kit) for its command-line interface, which allows you to add custom shell commands for your app.

- ItsDangerous security when sending data using cryptographical signing.

- Jinja2 is a powerful template engine for Python

- MarkupSafe is a HTML string handling library.

- Werkzeug is a utility library for WSGI, a protocol that ensures web apps and web servers can communicate effectively.

We can save this as a requirements.txt file by using the following line of code:
`pip freeze > requirements.txt`


# Let's Make a More Robust App
In the terminal let's set up to create a new app that's a bit closer to a standard set up.

In our terminal let's start creating some directories and files.
`mkdir app app/templates`

`touch run.py config.py`

`mkdir app`

`cd app`

`touch __init__.py views.py`

# Setting up our config.py file
In our config.py file let's add the following line of code.
```Python
DEBUG = True
```

# Setting up init file
In our `__init__.py` file let's add the following code:
```Python
# app/__init__.py

from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import views

# Load the config file
app.config.from_object('config')

```

# Views
In our views.py file we can add this code to set up our routes.

```Python
from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")
```

# Run
In our run.py file let's add the following
```
from app import app

if __name__ == '__main__':
    app.run()
```

# Templates
Let's go into the app directory and make some files.

`touch base.html index.html about.html`

In the base.html file we'll add the following:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>{% block title %}{% endblock %}</title>
    <!-- Bootstrap core CSS -->
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom styles for this template -->
    <link href="https://getbootstrap.com/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">
  </head>
  <body>
    <div class="container">
      <div class="header clearfix">
        <nav>
          <ul class="nav nav-pills pull-right">
            <li role="presentation"><a href="/">Home</a></li>
            <li role="presentation"><a href="/about">About</a></li>
            <li role="presentation"><a href="http://flask.pocoo.org" target="_blank">Built with Flask</a></li>
          </ul>
        </nav>
      </div>
      {% block body %}
      {% endblock %}
      <footer class="footer">
        <p>NYU Advanced Python Class</p>
      </footer>
    </div> <!-- /container -->
  </body>
</html>

```

In the index.html file we'll add this:
```html
{% extends "base.html" %}
{% block title %}Home{% endblock %}
{% block body %}
<div class="jumbotron">
  <h1>NYU Advanced Python</h1>
  <p class="lead">Our First Flask Site</p>
</div>
{% endblock %}
```

In the about.html file we'll add the following code:

```html
{% extends "base.html" %}
{% block title %}About{% endblock %}
{% block body %}
<div class="jumbotron">
  <h1>The About Page</h1>
  <p class="lead">This site was built in the NYU advanced python class.</p>
</div>
{% endblock %}
```

# Let's Make a Static Directory
Let's add an directory called static if we want add images, css, or JavaScript.

# Now We are Ready to Run our App
Let's export one more time and run our app.
```
export FLASK_APP=run.py
flask run
```
