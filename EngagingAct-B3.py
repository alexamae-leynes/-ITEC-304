from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args['name']
    return """
        <html><body>
            <h1><b>Welcome to Alexa's Resort</b></h1><br>
            <h><b>Name: {0}</b></h><br>
            <b>Time in at {1}.</b>
        </body></html>
        """.format(
            name, str(datetime.now()))

# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)
