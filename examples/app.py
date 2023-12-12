from smtplib import SMTP
from email.message import EmailMessage

from flask import Flask, request
import helpers

app = Flask(__name__)


@app.route("/handle-forgotten-password", methods=["POST", "GET"])
def handle_forgotten_password():
    email_address = request.values["email_address"]
    if helpers.verify_email_exists(email_address):
        link = helpers.generate_password_reset_link_for(email_address)
        msg = EmailMessage()
        msg["From"] = "support@allcapstyping.com"
        msg["To"] = email_address
        msg["Subject"] = "RESET YOUR PASSWORD NOW"
        msg.set_content(f"Here is your password reset link: {link}")
        with SMTP("smtp.allcapstyping.com") as smtp:
            smtp.send_message(msg)
    else:
        return False
