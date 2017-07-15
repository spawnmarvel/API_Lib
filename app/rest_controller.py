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
tasks = [
	{
		"id" : 1,
		"title" : u"tag2",
		"desciption" : "test2",
		"done" : False
	}
]

@app.route("/cmd/api/tasks", methods=["GET"])
def get_all_tasks():
    return jsonify({"tasks": tasks})

@app.route('/cmd/api/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201



@app.route("/cmd/api/data", methods=["GET"])
def get_all_data():
    return jsonify({"data": data})


@app.route("/cmd/api/data/<int:data_id>", methods=["GET"])
def get_data(data_id):
    tmp_data = [da for da in data if da["id"] == data_id]
    if len(tmp_data) == 0:
    	# call to improved abort function
        abort(404)
    return jsonify({"data": tmp_data[0]})

@app.route("/cmd/api/data", methods=["POST"])
def insert_data():
	print("start")
	if not request.json or not "name" in request.json:
		abort(400)
	tmp_data = {
				"id" : len(data) + 1,
				"name" : request.json["name"],
				"value" : request.json.get("value", ""),
				"quality" : request.json.get("quality", "")
	}
	data.append(tmp_data)
	return jsonify({"data" : data}), 201


@app.route("/")
def api_information():
	return render_template("index.html")

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({"error" : "Not found"}), 404)


if __name__ == "__main__":
    app.run(debug=True, port=6060)
