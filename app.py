from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello Karely"
 
if __name__ == "__main__":
    app.run()
  
  @app.route("/index")
  def index():
       return open("index.html").read()
