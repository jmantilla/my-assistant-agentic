from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Logic to retrieve data goes here
    return jsonify({"message": "Data retrieved successfully"}), 200

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.json
    # Logic to process the posted data goes here
    return jsonify({"message": "Data processed successfully", "data": data}), 201

if __name__ == '__main__':
    app.run(debug=True)