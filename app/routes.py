from app import app

@app.route("/")
def home ():
    return "Heloo World from Github Pages"
