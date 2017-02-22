from flask.views import MethodView
from flask import jsonify, request, abort

class PetAPI(MethodView):
    pets = [
        { "id": 1, "name": u"max" },
        { "id": 2,"name": u"Leo" },
        {"id": 3, "name": u"Jimi"}
    ]

    def get(self):
        return jsonify({"pets": self.pets})

    # def post(self):