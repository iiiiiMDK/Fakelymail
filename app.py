from flask import Flask, render_template, request, session, jsonify
import time, threading, random, string
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'

inboxes = {}

# توليد ايميل وهمي
def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = 'fakelymail.com'
    return f"{username}@{domain}"

# حذف الإيميل بعد مدة تلقائيًا
def auto_delete_email(email, lifetime=1800):
    time.sleep(lifetime)
    inboxes.pop(email, None)

@app.route('/')
def home():
    return render_template('home.html')  # لو عندك صفحة ترحيبية

@app.route('/email')
def index():
    if 'email' not in session:
        session['email'] = generate_email()
        inboxes[session['email']] = {
            'created_at': time.time(),
            'messages': []
        }
        threading.Thread(target=auto_delete_email, args=(session['email'],), daemon=True).start()

    email = session['email']
    if email not in inboxes:
        inboxes[email] = {
            'created_at': time.time(),
            'messages': []
        }
        threading.Thread(target=auto_delete_email, args=(email,), daemon=True).start()

    remaining = int(inboxes[email]['created_at'] + 1800 - time.time())
    return render_template('index.html', email=email, timer=remaining)

@app.route('/change')
def change_email():
    session.pop('email', None)
    return '', 204

@app.route('/messages')
def get_messages():
    email = session.get('email')
    if email and email in inboxes:
        return jsonify(inboxes[email]['messages'])
    return jsonify([])

@app.route('/receive', methods=['POST'])
def receive_email():
    data = request.form
    sender = data.get('sender')
    subject = data.get('subject')
    body = data.get('body-plain')
    email = data.get('recipient')

    if email in inboxes:
        inboxes[email]['messages'].append({
            'from': sender,
            'subject': subject,
            'body': body,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    print(f'New email for {email}\nFrom: {sender}\nSubject: {subject}\nBody:\n{body}')
    return 'OK', 200

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)