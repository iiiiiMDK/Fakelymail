from flask import Flask, render_template, request, session, jsonify
import time, threading, random, string
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'

inboxes = {}

# --------- Email Generator ---------
def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = 'fakelymail.com'
    return f"{username}@{domain}"

# --------- Email Auto-delete ---------
def auto_delete_email(email, lifetime=1800):
    time.sleep(lifetime)
    inboxes.pop(email, None)

# --------- Home Page ---------
@app.route('/')
def home():
    return render_template('home.html')

# --------- Email Page ---------
@app.route('/email')
def index():
    if 'email' not in session:
        session['email'] = generate_email()
        inboxes[session['email']] = {'created_at': time.time(), 'messages': []}
        threading.Thread(target=auto_delete_email, args=(session['email'],), daemon=True).start()

    email = session['email']
    if email not in inboxes:
        inboxes[email] = {'created_at': time.time(), 'messages': []}
        threading.Thread(target=auto_delete_email, args=(email,), daemon=True).start()

    remaining = int(inboxes[email]['created_at'] + 1800 - time.time())
    return render_template('index.html', email=email, timer=remaining)

# --------- Change Email ---------
@app.route('/change')
def change_email():
    session.pop('email', None)
    return '', 204

# --------- Messages API ---------
@app.route('/messages')
def messages():
    email = session.get('email')
    if not email or email not in inboxes:
        return jsonify([])
    return jsonify(inboxes[email]['messages'])

# --------- Mailgun Receive Webhook ---------
@app.route('/receive', methods=['POST'])
def receive_email():
    data = request.form
    recipient = data.get('recipient')
    sender = data.get('sender')
    subject = data.get('subject')
    body = data.get('body-plain')

    print(f'\n📨 Email Received!\nTo: {recipient}\nFrom: {sender}\nSubject: {subject}\nBody:\n{body}\n')

    if recipient not in inboxes:
        inboxes[recipient] = {
            'created_at': time.time(),
            'messages': []
        }

    inboxes[recipient]['messages'].append({
        'from': sender,
        'subject': subject,
        'body': body,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M')
    })

    return 'OK', 200

# --------- Run App (local) ---------
if __name__ == '__main__':
    app.run(debug=True)
