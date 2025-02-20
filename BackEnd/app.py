from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

# connect to mongodb
MONGO_URI = "mongodb+srv://leonardolin9943:<Password_hidden>@lighttukko.n41fv.mongodb.net/?retryWrites=true&w=majority&appName=Lighttukko"
client = MongoClient(MONGO_URI)
db = client["my_database"] 
collection = db["messages"] 

@app.route('/')
def home():
    return "Flask backend is running!"

@app.route('/submit', methods=['POST'])
def receive_message():
    data = request.json
    message = data.get('message')
    if not message:
        return jsonify({"error": "Empty Message"}), 400
    collection.insert_one({"message": message})
    
    return jsonify({"status": "success", "message": "Message is successfully stored in database!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
#LBfEghMlGrtHQ5kz