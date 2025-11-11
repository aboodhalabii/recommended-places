from  flask import flask , render_template, request , redirect, url_for
from stc.auth.service import recommendedServices

app = Flask(__name__)
recommended_services =recommendedServices()

@app.route('/')
def index():
    data = recommended_services.get_all_recommended()
    return render_template("index.html",tasks=data)


@app.route('/add', methods=["POST"])
def add_task():
    description = request.from["description"]
    location = request.from["location"]
    features = request.from["features"]

    if request.method == 'POST':
        return "This was a POST request."
    else:
        return "This was a GET request."
