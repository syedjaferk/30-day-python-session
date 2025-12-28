from flask import Flask, render_template, request, jsonify
from add import add_two_numbers
app = Flask(__name__)

@app.route("/<name>")
def home(name):
	# return "Hello World"
	return render_template("home.html", name=name)

@app.route("/add/<num1>/<num2>", methods=["GET", "POST"])
def add(num1, num2):
	num1 = int(num1)
	num2 = int(num2)
	result = add_two_numbers(num1, num2)
	return {"result": result}

@app.route("/search")
def search():
	name = request.args.get("name")
	age = request.args.get("age")

	return {"name": name, "age": age}



@app.route("/api/user", methods=["POST"])
def create_user():
	data = request.json
	data["message"] = "Processed"
	return jsonify(data)



if __name__ == "__main__":
	app.run(debug=True)