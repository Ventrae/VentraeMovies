from flask import Flask
from google.cloud import firestore
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

app = Flask(__name__)
db = firestore.Client()

apiKey = os.environ['SendGridApiKey']

@app.route("/tasks/cron/newsletter")
def newsletter():
	query_ref = db.collection("Users").where("newsletter", "==", True)
	user_emails = []
	for e in query_ref.stream():
		user_emails.append(e.to_dict()["email"])
	
	for email in user_emails:
		message = Mail(
			from_email="s16739@pjwstk.edu.pl",
			to_emails=email,
			subject="test-mail-vm",
			html_content="testowy mail ventrae-movies"
		)
		sg = SendGridAPIClient(apiKey)
		sg.send(message)

	return 'Succesfully sent newsletter', 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)