from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "id": 0,
        "name": "nikola",
        "email": "nikolailic02@gmail.com"
    },
    {
        "id": 1,
        "name": "proba",
        "email": "proba@gmail.com"
    },
    {
        "id": 2,
        "name": "david",
        "email": "davidbujic@gmail.com"
    }
]


class User(Resource):
    def get(self, idr):
        for user in users:
            if idr == user["id"]:
                return user, 200
        return "User not found", 404

    def post(self, idr):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("email")
        args = parser.parse_args()

        for user in users:
            if idr == user["id"]:
                return "User with id  {} already exists".format(idr), 400

        user = {
            "id": idr,
            "name": args["name"],
            "email": args["email"]
        }
        users.append(user)
        return user, 201

    def put(self, idr):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("email")
        args = parser.parse_args()

        for user in users:
            if idr == user["id"]:
                user["name"] = args["name"]
                user["email"] = args["email"]
                return user, 200

        user = {
            "id": idr,
            "name": args["name"],
            "email": args["email"]
        }
        users.append(user)
        return user, 201

    def delete(self, idr):
        global users
        users = [user for user in users if user["id"] != idr]
        return "{} is deleted".format(idr), 200


api.add_resource(User, '/user/<int:idr>')

if __name__ == '__main__':
    app.run(debug=True)