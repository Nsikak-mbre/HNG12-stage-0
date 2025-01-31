from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS
from flask_compress import Compress


app = Flask(__name__)
CORS(app)
Compress(app)

@app.route("/", methods=["GET"])
def get_info():
    response = {
        "email": "nsikakmbre@gmail.com",
        "current_datetime": datetime.utcnow().isoformat(),
        "github_url": "git@github.com:Nsikak-mbre/HNG12-stage-0.git"
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
