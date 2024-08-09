# Importing flask module in the project is mandatory
from flask import Flask
import os

# An object of Flask class is our WSGI application.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call the associated function.
@app.route('/')
def hello_world():
    return 'Hello World'

# Main driver function
if __name__ == '__main__':
    # Get the port from environment variables (Azure sets this automatically)
    
    
    # Run the app on the specified port, accessible from any network interface
    app.run()
