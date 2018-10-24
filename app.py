from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello Karely"
@app.route("/index")
def index():
    return open("index.html").read()

if __name__ == "__main__":
    app.run()
  
 
