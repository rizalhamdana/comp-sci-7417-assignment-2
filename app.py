from flask import Flask, request, redirect
import requests

app = Flask(__name__)

CLIENT_ID = "31620"
CLIENT_SECRET = "sVAncuI*uwmPRLwhBZ9lNQ(("
REDIRECT_URI = "https://5a61-210-5-32-245.ngrok-free.app/callback"

@app.route("/")
def login():
    auth_url = f"https://stackoverflow.com/oauth?client_id={CLIENT_ID}&scope=read_inbox,private_info&redirect_uri={REDIRECT_URI}"
    return redirect(auth_url)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    token_url = "https://stackoverflow.com/oauth/access_token/json"
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "redirect_uri": REDIRECT_URI
    }
    response = requests.post(token_url, data=data)
    access_token = response.json().get("access_token")
    return f"Access Token: {access_token}"

if __name__ == "__main__":
    app.run(port=80, debug=True)
