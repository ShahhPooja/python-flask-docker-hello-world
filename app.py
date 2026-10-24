from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return """<html>
<head>
<title>My DevOps Project</title>
</head>
<body style="background:linear-gradient(135deg,#667eea,#764ba2);font-family:Arial;text-align:center;padding:80px;">

<div style="background:white;padding:40px;border-radius:20px;max-width:650px;margin:auto;box-shadow:0 10px 30px #444;">

<h1 style="color:#5b4bdb;">🚀 My DevOps Project</h1>

<h2>Automated CI/CD Pipeline</h2>

<p>GitHub → Jenkins → Docker → AWS EC2</p>

<h3 style="color:green;">✅ Deployment Successful!</h3>

<button style="background:#667eea;color:white;padding:15px 30px;border:0;border-radius:10px;font-size:16px;">
CI/CD Working Successfully
</button>

</div>
</body>
</html>"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
