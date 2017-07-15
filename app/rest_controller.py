from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import render_template

app = Flask(__name__)

# simulating db
data = [
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


@app.route("/cmd/api/data", methods=["GET"])
def get_all_data():
    return jsonify({"data": data})


@app.route("/cmd/api/data/<int:data_id>", methods=["GET"])
def get_data(data_id):
    tmp_data = [da for da in data if da["id"] == data_id]
    if len(tmp_data) == 0:
        abort(404)
    return jsonify({"data": tmp_data[0]})

@app.route("/cmd/api/data", methods=["POST"])
def insert_data():
	if not request.json or not "name" in request.json or not "value" in request.json or not "quality" in request.json:
		abort(400)
	else:
		tmp_data = {
				"id" : len(data) + 1,
				"name" : request.json["name"],
				"value" : request.json["value"],
				"quality" : request.json["quality"]
		}
	data.append(tmp_data)
	return jsonify({"data" : data}), 201

@app.route('/cmd/api/data/<int:data_id>', methods=['PUT'])
def update_data(data_id):
    tmp = [da for da in data if da["id"] == data_id]
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
    tmp = [da for da in data if da["id"] == data_id]
    if len(tmp) == 0:
        abort(404)
    data.remove(tmp[0])
    return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({"error" : "Not found"}), 404)

@app.errorhandler(400)
def not_found(error):
	return make_response(jsonify({"error" : "Bad request"}), 400)


if __name__ == "__main__":
    app.run(debug=True, port=6060)
