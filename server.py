import requests
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/users', methods=["GET", "POST"])
def hello(*args, **kwargs):
    resp = requests.get("http://localhost:8080/auth/realms/MyDemo/protocol/openid-connect/userinfo", headers={
        "Authorization": request.headers["Authorization"],
    })
    resp.raise_for_status()
    return resp.content

if __name__ == "__main__":
    app.run(debug=True, port=9000)
