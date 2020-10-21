from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome Azure App Service Demo ! '


if __name__ == '__main__':
    app.run()

