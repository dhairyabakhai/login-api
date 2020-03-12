from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate
from user import User


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate)



if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True




