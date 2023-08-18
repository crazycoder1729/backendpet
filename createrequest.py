from flask import Flask, jsonify, request
import data
from flask_cors import CORS
from upload import upload
app = Flask(__name__)
CORS(app)
@app.route("/data", methods=["GET"])
def get_example():
    k = data.collect_data(request.args.get('ele'))
    return jsonify(k)

@app.route('/add_data/<string:data>', methods=['POST'])
def add_data(data):
    try:
        findata = request.json  # Assuming JSON data in the POST request body
        upload(findata,type=data)
        # print(data)
        return jsonify({"message": "Data added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
