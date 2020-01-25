from flask import Flask
from google.cloud import firestore


app = Flask(__name__)
db = firestore.Client()


@app.route("/tasks/cron/newsletter")
def newsletter():
	print('i cron it')
	return 'croned', 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)