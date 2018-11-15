
#import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

# client interact with resource directly
# resource is external
# Resource is used to map endpoints
# find_by_name, insert, update are from models package

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price",
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
    )

    parser.add_argument("store_id",
                        type=int,
                        required=True,
                        help="Every item needs a store id."
    )

    # CRUD : Read, SELECT * FROM
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name) # it returns an item object
        if item:
            return item.json()
        return {"message": "Item not found"}, 404
    
    # CRUD : Create, INSERT INTO
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
        # 400 : something went wrong with the request
        #item = {'name': name, 'price': 12.00}

        data = Item.parser.parse_args()
        
        #data = request.get_json(force=True) # you don't need content-type header
        #data = request.get_json(silent=True)
        #####data = request.get_json()
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except:
            return {"message": "An error occured inserting the item."}, 500 # Internal Server Error
            
        return item.json(), 201
    
    # CRUD : Delete, DELETE FROM
    #@jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
    
        return {"message": "Item deleted"}

    # wait : check put method
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
                
        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data["price"]

        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        #return {"items": [item.json() for item in ItemModel.query.all()]}
        return {"items": list(map(lambda x: x.json(), ItemModel.query.all()))}
    
