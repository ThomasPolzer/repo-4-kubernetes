from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask Version 03 exclusive from Kubernetes CI/CD-Pipeline!'

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080)
