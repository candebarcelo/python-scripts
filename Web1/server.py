from flask import Flask, render_template # render_template is to use html file(s)

app = Flask(__name__) # we instantiate app as a Flask class item. __name__ is __main__ when we run this file

@app.route("/") # decorator. when we do the url ending in / (home page) it shows this string.
def homepage():
    return render_template('index.html') # this automatically looks for the index.html inside a templates 
                                         # folder, so be sure to store it there

@app.route("/about") # if your site's url ends in /about, it'll show this
def about():
    return render_template('about.html') 

@app.route("/<username>") 
def hello(username=None): # username defaults to none if it's not entered
    return render_template('index.html', name=username) 

