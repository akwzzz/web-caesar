from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!doctype html>
<html>
    <body>
        <form action="/hello" method="post">
            <label for="first-name">First Name:</label>
            <input id="first-name" type="text" name="first_name" />
            <input type="submit" />
        </form>
    </body>
</html>
"""
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form method="post">
      <label>Rotate by:
        <input type="text" name="rot" value="0" />
        <textarea name="text"></textarea>
        <input type="submit" />
        </label>
      </form>
    </body>
</html>
"""



@app.route("/")
def index():
    return form

@app.route("/hello", methods=['post'])
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, ' + first_name + '</h1>'

@app.route("/", methods=['post'])
def encrypt():
    text = str(request.form['text'])
    rot = int(request.form['rot'])
    new_text = ''
    for i in text:
        new_text += rotate_string(i, rot)
    return '<h1>' + new_text + '</h1>'


app.run()