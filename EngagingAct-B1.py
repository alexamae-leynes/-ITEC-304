from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
        <html>
        <style>
            body{
            background-color:#000000;
            }
            h1{
            font-size:70px;
            animation-name: example;
            animation-duration: 10s;
            text-align:center;
            padding:50px;
            }
            @keyframes example {
            from {color: #34eb3a;}
            to {color: #dc34eb;}
            }
            a:hover, a:active {
             color: #c20c0c;
            }
            h2{
            color:#ffffff;
            font-size:50px;
            text-align:center;
            }
            </style>
            <body>
            <h1>Hello, Alexa!</h1>
            <h2>Click <a href="/message">here</a> for the message.</h2>
        </body></html>
        """
@app.route('/message')
def message():
    return """
        <html>
        <style>
        body{
        background-color:#000000;
        color:#ffffff;
        font-size:50px;
        text-align:center;
        padding:200px;
        }
        </style>
        <body>
            It's alright! You can do it. Just do what you love!
        </body></html>
        """

# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)
