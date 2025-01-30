from flask import Flask, jsonify
from datetime import datetime
import pytz
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def get_info():
    response = {
        "email": "nsikakmbre@gmail.com",
        "current_datetime": datetime.now(pytz.utc).isoformat(),
        "github_url": "https://github.com/yourusername/your-repo"
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
