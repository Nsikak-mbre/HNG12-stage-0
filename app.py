from flask import Flask, Response
import orjson
from datetime import datetime, timezone
from flask_cors import CORS
from flask_compress import Compress


app = Flask(__name__)
CORS(app)
Compress(app)
app.config["COMPRESS_LEVEL"] = 9  # Max compression
app.config["COMPRESS_MIN_SIZE"] = 512  # Min size to compress in bytes

def orjson_response(data, status=200):
    return Response(
        orjson.dumps(data),
        status=status,
        mimetype="application/json"
    )

@app.route("/", methods=["GET"])
def get_info():
    response = {
        "email": "nsikakmbre@gmail.com",
        "current_datetime": datetime.now(timezone.utc).isoformat(),
        "github_url": "git@github.com:Nsikak-mbre/HNG12-stage-0.git"
    }
    return orjson_response(response)

if __name__ == "__main__":
    app.run(debug=False, port=5000)
