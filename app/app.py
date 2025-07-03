from flask import Flask
# Creates the app. _name_ - special python variable, represents the name of the current file
app = Flask(__name__)   

# Defines a URL path. route decorator -  when someone visits the root URL (/), call the hello() function.
@app.route('/')     

def hello():
    return "Hello from DevOps!"

if __name__ == '__main__':
    # app.run(...) starts the web server.
    app.run(host='0.0.0.0', port=5000)  
    