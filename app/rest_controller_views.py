from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import render_template
from flask import url_for
from flask.ext.httpauth import HTTPBasicAuth
# from flask_sqlalchemy import SQLAlchemy

from app import app
auth = HTTPBasicAuth()

# simulating db
data_repos = [
    {
        "id": 1,
        "name": u"tag1",
                "value": 492.2,
                u"quality": "good"

    },
    {
        "id": 2,
        "name": u"tag2",
                "value": 692.2,
                u"quality": "good"
    }
]


@app.route("/")
def api_information():
    return render_template("index.html")


@auth.get_password
def get_password(username):
    if username == "espen":
        return "python"
    return None


@app.route("/cmd/api/data", methods=["GET"])
# @auth.login_required
def get_all_data():
    # return jsonify({"data": data_repos})
    return jsonify({"data" : [make_public(d) for d in data_repos]})


@app.route("/cmd/api/data/<int:data_id>", methods=["GET"])
def get_data(data_id):
    tmp_data = [da for da in data_repos if da["id"] == data_id]
    if len(tmp_data) == 0:
        abort(404)
    return jsonify({"data": tmp_data[0]})


@app.route("/cmd/api/data", methods=["POST"])
def insert_data():
    if not request.json or not "name" in request.json or not "value" in request.json or not "quality" in request.json:
        abort(400)
    else:
        tmp_data = {
            "id": len(data_repos) + 1,
            "name": request.json["name"],
            "value": request.json["value"],
            "quality": request.json["quality"]
        }
    data_repos.append(tmp_data)
    return jsonify({"data": data_repos}), 201


@app.route('/cmd/api/data/<int:data_id>', methods=['PUT'])
def update_data(data_id):
    tmp = [da for da in data_repos if da["id"] == data_id]
    print(str(tmp))
    if len(tmp) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if "name" in request.json and type(request.json["name"]) is not str:
        abort(400)
    if "quality" in request.json and type(request.json['quality']) is not str:
        abort(400)
    if "value" in request.json and type(request.json["value"]) is not int:
        abort(400)
    tmp[0]["name"] = request.json.get("name", tmp[0]["name"])
    tmp[0]["quality"] = request.json.get("quality", tmp[0]["quality"])
    tmp[0]["value"] = request.json.get("value", tmp[0]["value"])
    print(str(tmp))
    return jsonify({'PUT tmp': tmp[0]})


@app.route('/cmd/api/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    tmp = [da for da in data_repos if da["id"] == data_id]
    if len(tmp) == 0:
        abort(404)
    data.remove(tmp[0])
    return jsonify({'result': True})

# Improving the web service:
# Insted of returning id's, we can return the full URI that controls the data row
# So this will not prevent us from making changes to URI in the future
# The client get the URI ready to be used
def make_public(data_row):
    data_new = {}
    for d in data_row:
        if d == "id":
            data_new["uri"] = url_for("get_all_data",data_row_id=data_row["id"], external=True )
        else:
            data_new[d] = data_row[d]
    return data_new


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({"error": "Bad request"}), 400)


@app.errorhandler(405)
def not_found(error):
    return make_response(jsonify({"error": "Method not allowed"}), 405)


@auth.error_handler
def unauthorized():
    return make_response(jsonify({"error": "Unauthorized access"}), 403)
# if __name__ == "__main__":
#    app.run(debug=True, port=6060)
