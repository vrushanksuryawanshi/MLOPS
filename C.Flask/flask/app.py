from flask import Flask

"""
It creates an instance of the Flask class,
which will be your WSGI(web server gateway interface) application.
"""
#WSGI APPLICATION
app=Flask(__name__)



@app.route("/")
def welcome():
    return "Welcome to this flask course"

@app.route("\index")
def index():
    return "this is the index page of my flask"

"""
This is the entry point of any .py file in entire code, 
it will check this and execution starts from here
"""
if __name__=="__main__":
    app.run()
    