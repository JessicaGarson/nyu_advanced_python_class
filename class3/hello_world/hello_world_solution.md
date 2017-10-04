# Hello World

Let's make a file called hello_world.py
```Python
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'
```

To run this file export the file
`export FLASK_APP=hello_world.py`

And than type the following into your terminal
`python -m flask run`
