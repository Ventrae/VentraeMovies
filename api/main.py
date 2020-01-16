from flask import Flask, jsonify, session, redirect, request
from google.cloud import firestore, tasks_v2
import secrets
import hashlib
import json
import time
from datetime import datetime

db = firestore.Client()
app = Flask(__name__)
app.config["SECRET_KEY"] = "432de2a86dab9bf1781b484f3199620d712bc61c533f8d0c0c6a62b3003713e28796e4418a5884c55584ea0b8d23ca3f02dc"
    
@app.route("/api/login", methods=["POST"])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    if(email == '' or password == ''):
        return {
            'Alert': 'Email or password cannot be empty',
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
            return 'You are already logged in', 400

    if session.get('token'):
        return 'You are already logged in', 400

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
    return 'Wrong email or password', 400

@app.route('/api/logout', methods=['POST'])
def logout():
    if 'token' in session:
        usersOnline = db.collection(u'UsersOnline')
        users = usersOnline.stream()
        for user in users:
            if user.to_dict()['token']==session['token']:
                usersOnline.document(user.id).delete()
                session.pop('token', None)
                return 'Logged out', 200
    else:
        return 'You are NOT logged in', 401

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
    communicat = 'Email already in use!'

    if (email == '' or password == ''):
        return {
            'Alert': 'Email or password cannot be empty',
        }, 400

    for doc in docs:
        if email == doc.to_dict()['email']:
            return jsonify(communicat), 400

    data = {
        'email': email,
        'password': password.hexdigest(),
        'activated' : False,
        'registrationTimeStamp' : dateTime_object,
    }

    db.collection(u'Users').add(data)
    return 'Success', 200

@app.route("/api/recomendations/<id>", methods=["GET"])
def recomend():
    url = "https://api.themoviedb.org/3/movie/578?api_key=ae3d804c4aed5b48745ca5d2de0c0294&language=pl-PL"
    return jsonify(url), 200

@app.route("/api/rate", methods=["POST"])
def rate():
    data = request.json
    rateTime = time.time()
    dtObject = datetime.fromtimestamp(rateTime)
    rating = {
        'user': data.get('user'),
        'movie': data.get('movie'),
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
    else:
        db.collection(u'Ratings').document(a[0]["id"]).set(rating)
    return "Successfully rated a movie", 200

# @app.route("/api/mail", methods=["GET"])
# def f_mail():
#     client = tasks_v2.CloudTasksClient()
#     parent = client.queue_path("sandbox-264214", "europe-west3", "mail")
#     payload = json.dumps(people, ensure_ascii=False).encode()
#     task = {
#         "app_engine_http_request": {
#             "http_method": "POST",
#             "app_engine_routing": {
#                 "service": "tasks-worker"
#             },
#             "relative_uri": "/tasks/mail",
#             "headers": {
#                 "Content-Type": "application/json"
#             },
#             "body": payload
#         }
#     }
#     client.create_task(parent, task)
#     return "Wysłano maila z listą osób", 200


# @app.route("/api/movies/", methods=["GET"])
# def f_people():
#     if "logged" in session:
#         if session["logged"] == True:
#             return jsonify(people), 200
#         else:
#             session["logged"] = False
#             return "Użytkownik niezalogowany", 401
#     else:
#         session["logged"] = False
#         return "Użytkownik niezalogowany", 401


# @app.route("/api/movies/<id>", methods=["GET"])
# def f_person(id):
#     if "logged" in session:
#         if session["logged"] == True:
#             if int(id) < people.__len__():
#                 return jsonify(people[int(id)]), 200
#             else:
#                 return redirect("/api/people/", code=302)
#         else:
#             session["logged"] = False
#             return "Użytkownik niezalogowany", 401
#     else:
#         session["logged"] = False
#         return "Użytkownik niezalogowany", 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
