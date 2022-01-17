from flask import Flask, redirect, url_for
# redirect, url_for : if we want to redirect different pages from our code

# Create an instance of a Flask web application
app = Flask(__name__)

# Define how we can access the specific page. We have to give a route
# Decorate the function (see decorators)
@app.route("/")
# / or /home , when we go to our default domain, it will automatically send us to the home page

# Define the pages of the website
def home():
    # This is the html
    return "Hello! this is the main page <h1>HELLO<h1>"

@app.route("/<name>") # This is a decorator
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home")) # It redirects to home page

# Run the app
if __name__ == "__main__":
    app.run()
