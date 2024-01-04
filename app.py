from flask import Flask, request, jsonify
from operations import *

app = Flask(__name__)

@app.route("/")
def greet():
    return "Welcome to Your Class..."


@app.route("/v1/add", methods=["POST"])
def add():
    try:
        name = request.json["name"],
        standard = request.json["standard"]
        fees = request.json["fees"]
        add_student([name, standard, fees])
        return f"Student : {name} has been added successfully to the records.", 201

    except Exception as error:
        return f"Could not add Student because, {error}", 400


@app.route("/v1/retrieve/<string:id>", methods=["GET"])
def retrieve(id):
    try:
        data = retrieve_data(id)
        if data :
            return jsonify(data), 201
        else:
            return f"Student Not Found, {error}", 404

    except Exception as error:
        return f"Could not retrieve Student Data because, {error}", 400


@app.route("/v1/update/<string:id>", methods=["PATCH"])
def update(id):
    try:
        name = request.json["name"],
        standard = request.json["standard"],
        fees = request.json["fees"]
        update_data((name, standard, fees, id))
        return f"Student with Student_Id : {id} has been Updated Successfully", 201

    except Exception as error:
        return f"Could not Update Student Data because, {error}", 400


@app.route("/v1/delete/<string:id>", methods=["DELETE"])
def delete(id):
    try:
        remove_data(id)
        return f"Student with Student_Id : {id} has been removed successfully from the records.", 201

    except Exception as error:
        return f"Could not remove Student becasue, {error}", 400


@app.route("/v1/pay/<string:id>", methods=["POST"])
def pay(id):
    try:
        status = request.json["status"]
        pay_fees(id, status)
        return f"Fees Paid Successfully", 201

    except Exception as error:
        return f"Could not Pay fees because, {error}", 400


if __name__ == "__main__":
    app.run(debug=True)