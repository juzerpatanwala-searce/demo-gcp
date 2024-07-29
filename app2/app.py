from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'App deployed on Cloud Run'

if __name__ == '__main__':
    # Listen on all interfaces and port 80
    app.run(host='0.0.0.0', port=80)
