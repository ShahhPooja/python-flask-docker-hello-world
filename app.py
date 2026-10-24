from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
  return "<h1>My Cloud Computing & DevOps Project</h1><p>Automated CI/CD using GitHub, Jenkins, Docker and AWS EC2</p><p>Deployment Successful!</p>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
