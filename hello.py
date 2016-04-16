import os
from flask import Flask, render_template, request
from flask_mail import Mail, Message


app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tt7976897@gmail.com'
app.config['MAIL_PASSWORD'] = 'testeapp123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/sendMail")
def sendMail():
    try:
	sendTo = request.args.get('sendTo')
	sendWhat = request.args.get('sendWhat')
	print sendTo
	print sendWhat
	msg = Message('Hello', sender = 'tt7976897@gmail.com', recipients = [sendTo])
   	msg.body = sendWhat
   	mail.send(msg)
	return 'sent'
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
