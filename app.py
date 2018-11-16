
import os
os.environ["FLASK_ENV"] = "development"
# set the FLASK_ENV environmental variable to development instead of production

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
# look into resourcs package, item module


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "jose"
api = Api(app)

jwt = JWT(app, authenticate, identity) # http://127.0.0.1:5000/auth endpoint

# authenticate, identity are defined in security
# this gives a long key for authentication

api.add_resource(Store, "/store/<string:name>")
api.add_resource(Item, '/item/<string:name>')
# for this endpoint JWT is required
# in Headers KEY: Authorization, VALUE : JWT xxxxxxx
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, "/stores")
api.add_resource(UserRegister, '/register')

# JWT : Jason Web Token
# 200 OK
# 201 CREATED
# 404 NOT FOUND

# to give JWT Headers
# KEY : Authorization
# Value : JWT long key


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    print("FLASK_ENV : ", os.environ.get("FLASK_ENV")) # why this print is coming twice
    app.run(port=5000, debug=True, use_reloader=False)


