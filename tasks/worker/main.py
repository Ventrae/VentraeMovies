from flask import Flask, request
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

app = Flask(__name__)

apiKey = os.environ['SendGridApiKey']

@app.route("/tasks/mail", methods=["POST"])
def mail():
    #data = request.json
    message = Mail(
        from_email="s16739@pjwstk.edu.pl",
        to_emails="s16739@pjwstk.edu.pl",
        subject="test-mail-vm",
        html_content="testowy mail ventrae-movies"
    )
    sg = SendGridAPIClient(apiKey)
    sg.send(message)
    return "", 200
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)