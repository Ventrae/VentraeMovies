from flask import Flask, jsonify, session, redirect, request
from google.cloud import firestore, tasks_v2, bigquery, language
from google.cloud.language import enums, types
from datetime import datetime
import secrets
import hashlib
import json
import time
import requests

db = firestore.Client()
app = Flask(__name__)
app.config["SECRET_KEY"] = "432de2a86dab9bf1781b484f3199620d712bc61c533f8d0c0c6a62b3003713e28796e4418a5884c55584ea0b8d23ca3f02dc"

# --- Account management endpoints: ---

@app.route("/api/login", methods=["POST"])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    if(email == '' or password == ''):
        return {
            'Alert': 'Email lub hasło nie może być puste.',
        }, 400

    password = hashlib.sha256(password.encode("UTF-8"))
    
    query_ref = db.collection(u'Users').where("email", "==", email)
    online_query_ref = db.collection(
            u'UsersOnline').where("email", "==", email)

    users = query_ref.stream()
    usersOnline = online_query_ref.stream()

    for user in usersOnline:
        if email == user.to_dict()['email']:
            print(user.to_dict()['email'])
            return 'Jesteś już zalogowany.', 400

    if session.get('token'):
        return 'Jesteś już zalogowany.', 400

    for user in users:
        if email == user.to_dict()['email'] and user.to_dict()['password'] == password.hexdigest():
            token = secrets.token_urlsafe(20)
            session['token'] = token
            db.collection('UsersOnline').add({
                'token': token,
                'email': user.to_dict()['email']
            })
            result = {
        		'id': user.id,
        		'token': token,
        		'email': email
            }
            return jsonify(result), 200
    return 'Niepoprawny email lub hasło.', 400

@app.route('/api/logout', methods=['POST'])
def logout():
    if 'token' in session:
        usersOnline = db.collection(u'UsersOnline')
        users = usersOnline.stream()
        for user in users:
            if user.to_dict()['token']==session['token']:
                usersOnline.document(user.id).delete()
                session.pop('token', None)
                return 'Wylogowano', 200
    else:
        return 'Nie jesteś zalogowany', 401

@app.route('/api/register', methods=['POST'])
def register():

    data = request.json
    email = data.get('email')
    password = data.get('password')
    password = hashlib.sha256(password.encode("UTF-8"))
    timestamp = time.time()
    dateTime_object = datetime.fromtimestamp(timestamp)
    
    query_ref = db.collection(u'Users').where("email", "==", email)
    docs = query_ref.stream()
    communicat = 'Ten adres email należy już do innego użytkownika!'

    if (email == '' or password == ''):
        return {
            'Alert': 'Email lub hasło nie mogą być puste.',
        }, 400

    for doc in docs:
        if email == doc.to_dict()['email']:
            return jsonify(communicat), 400

    data = {
        'email': email,
        'password': password.hexdigest(),
        'time' : dateTime_object,
        'newsletter': True
    }

    db.collection(u'Users').add(data)
    return 'Rejestracja udana!', 200

@app.route('/api/change-password', methods=['POST'])
def changePassword():
    return 'Hasło zostało zmienione', 200

@app.route('/api/change-email', methods=['POST'])
def changeEmail():
    return 'Adres email został zmieniony', 200

@app.route('/api/toggle-newsletter', methods=['POST'])
def toggleNewsletter():
    return 'Ustawienia newslettera zaktualizowane', 200

@app.route('/api/delete-account', methods=['POST'])
def deleteAccount():
    return 'Konto usunięte', 200

# --- Movies recommendations endpoints: ---

@app.route("/api/recommendations", methods=["GET"])
def recomend():

    user = request.args["user"]
    # limitowane do rekomendacji do 10 filmów (najlepiej ocenionych, najbardziej ostatnio)
    query_ref = db.collection("Ratings").where("user", "==", user).order_by(u'rate', direction=firestore.Query.DESCENDING).order_by(u'time', direction=firestore.Query.DESCENDING).limit(10)

    ratings = []
    for e in query_ref.stream():
        ratings.append(e.to_dict())

    recommendations = []
    url = "https://api.themoviedb.org/3/movie/{}/similar?api_key=ae3d804c4aed5b48745ca5d2de0c0294&language=en-US&page=1"
    for e in ratings:
        response = requests.request("GET", url.format(e["movie"]))
        body = json.loads(response.text)
        for sm in body["results"]:
            recommendations.append({
                'movie': sm["id"],
                'poster': 'https://image.tmdb.org/t/p/w600_and_h900_bestv2' + sm["poster_path"],
                'title': sm["title"]
            })
            
    seen = set()
    reccs_no_dupes = []
    for d in recommendations:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            reccs_no_dupes.append(d)

    return jsonify(reccs_no_dupes), 200

@app.route("/api/rate", methods=["POST"])
def rate():
    data = request.json
    rateTime = time.time()
    dtObject = datetime.fromtimestamp(rateTime)
    rating = {
        'user': data.get('user'),
        'movie': data.get('movie'),
        'title': data.get('title'),
        'rate': data.get('rating'),
        'time': dtObject,
    }
    
    query_ref = db.collection(u'Ratings').where("user", "==", data.get('user')).where("movie", "==", data.get('movie'))
    docs = query_ref.stream()

    a=[]
    for o in docs:
        a.append({"id":o.id,"data":o.to_dict()})

    if not a:
        db.collection(u'Ratings').add(rating)
        client = bigquery.Client()
        table_ref = client.get_table("projektarc.BigQueryData.MoviesRatings")
        ret = {
            'user': data.get('user'),
            'movie': data.get('movie'),
            'title': data.get('title'),
            'rate': data.get('rating'),
            'time': rateTime,
        }
        rowns = client.insert_rows_json(table_ref, [ret])
        print("BQ Errors:", rowns)
    else:
        db.collection(u'Ratings').document(a[0]["id"]).set(rating)
    return "Pomyślnie oceniono film", 200

@app.route("/api/rating", methods=["GET"])
def getRating():
    user = request.args["user"]
    movie = request.args["movie"]
    rating = 0
    query_ref = db.collection(u'Ratings').where(u"user", u"==", user).where(u"movie", u"==", int(movie))
    docs = query_ref.stream()
    a=[]
    for o in docs:
        a.append(o.id)
    if not a:
        rating = 0
    else:
        rating = db.collection(u'Ratings').document(a[0]).get().to_dict()["rate"]
    return jsonify(rating), 200

@app.route("/api/ratings", methods=["GET"])
def getRatingsList():

    user = request.args["user"]
    # limitowane do 20 ratingów
    query_ref = db.collection("Ratings").where("user", "==", user).order_by(u"time", direction=firestore.Query.DESCENDING).limit(20)
    ratings = []
    for e in query_ref.stream():
        ratings.append(e.to_dict())

    ratings_full = []
    url = "https://api.themoviedb.org/3/movie/{}?api_key=ae3d804c4aed5b48745ca5d2de0c0294&language=en-US"
    for e in ratings:
        response = requests.request("GET", url.format(e["movie"]))
        body = json.loads(response.text)
        print(e)
        ratings_full.append({
            'id': int(body["id"]),
            'title': body["title"],
            'rating': float(e["rate"]),
            'poster': 'https://image.tmdb.org/t/p/w600_and_h900_bestv2' + body["poster_path"]
        })
            
    return jsonify(ratings_full), 200

@app.route("/api/mail", methods=["GET"])
def mail():

    user = request.args["user"]
    # limitowane do rekomendacji do 5 filmów (najlepiej ocenionych, najbardziej ostatnio)
    query_ref = db.collection("Ratings").where("user", "==", user).order_by(u'rate', direction=firestore.Query.DESCENDING).order_by(u'time', direction=firestore.Query.DESCENDING).limit(5)

    ratings = []
    for e in query_ref.stream():
        ratings.append(e.to_dict())

    recommendations = []
    url = "https://api.themoviedb.org/3/movie/{}/similar?api_key=ae3d804c4aed5b48745ca5d2de0c0294&language=en-US&page=1"
    for e in ratings:
        response = requests.request("GET", url.format(e["movie"]))
        body = json.loads(response.text)
        for sm in body["results"]:
            recommendations.append({
                'movie': sm["id"],
                'poster': 'https://image.tmdb.org/t/p/w600_and_h900_bestv2' + sm["poster_path"],
                'title': sm["title"]
            })
            
    seen = set()
    reccs_no_dupes = []
    for d in recommendations:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            reccs_no_dupes.append(d)

    client = tasks_v2.CloudTasksClient()
    parent = client.queue_path("projektarc", "europe-west3", "mail")
    payload = json.dumps(reccs_no_dupes, ensure_ascii=False).encode()
    task = {
        "app_engine_http_request": {
            "http_method": "POST",
            "app_engine_routing": {
                "service": "tasks-worker"
            },
            "relative_uri": "/tasks/mail",
            "headers": {
                "Content-Type": "application/json"
            },
            "body": payload
        }
    }
    client.create_task(parent, task)
    return "Wysłano maila z rekomendowanymi filmami", 200

@app.route("/api/comment", methods=["GET"])
def getComments():
    movie = request.args["movie"]
    query_ref = db.collection("Comments").where("movie","==",int(movie))

    comments = []
    for e in query_ref.stream():
        comments.append(e.to_dict())
    return jsonify(comments), 200

@app.route("/api/comment", methods=["POST"])
def addComment():
    data = request.json
    rateTime = time.time()
    dtObject = datetime.fromtimestamp(rateTime)
    positivity = 0
    client = language.LanguageServiceClient()

    document = types.Document(content=data.get('content'),type=enums.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    positivity = sentiment.score*100

    comment = {
        'author': data.get('author'),
        'content': data.get('content'),
        'positivity': round(positivity,0),
        'time': dtObject,
        'movie': int(data.get('movie'))
    }
    db.collection("Comments").add(comment)
    return "Pomyślnie dodano komentarz", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
