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
    },
    {
        "id": 3,
        "name": u"tag3",
                "value": 25.4,
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


@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({"error" : "Not found"}), 404)

@app.errorhandler(400)
def not_found(error):
	return make_response(jsonify({"error" : "Bad request"}), 400)


if __name__ == "__main__":
    app.run(debug=True, port=6060)
