from flask import Flask, request, render_template, jsonify, session, redirect
import random
import string
import time
import threading

app = Flask(__name__)
app.secret_key = 'supersecretkey'

inboxes = {}

def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = 'fakelymail.com'
    return f'{username}@{domain}'

def auto_delete_email(email, lifetime=300):
    time.sleep(lifetime)
    inboxes.pop(email, None)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/email')       
def index():

@app.route('/receive', methods=['POST'])
def receive_email():
    data = request.form
    sender = data.get('sender')
    subject = data.get('subject')
    body = data.get('body-plain')

    print(f'📨 Email Received!\nFrom: {sender}\nSubject: {subject}\nBody:\n{body}')

    # احفظ الرسالة في صندوق الوارد لو المستخدم موجود
    email = session.get('email')
    if email in inboxes:
        inboxes[email]['messages'].append({
            'from': sender,
            'subject': subject,
            'body': body,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        })

    return 'OK', 200
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

@app.route('/privacy')  # <-- ضيف هذا هنا بالضبط
def privacy():
    return render_template('privacy.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

    if email not in inboxes:
        inboxes[email] = {
            'created_at': time.time(),
            'messages': []
        }
        threading.Thread(target=auto_delete_email, args=(email,), daemon=True).start()

    remaining = int(inboxes[email]['created_at'] + 1800 - time.time())
    return render_template('index.html', email=email, timer=remaining)
    return render_template('index.html', email=email, timer=remaining)

@app.route('/change')
def change_email():
    from datetime import datetime

@app.route('/receive', methods=['POST'])
def receive_email():
    email = request.form.get('recipient')
    subject = request.form.get('subject')
    body = request.form.get('stripped-text')
    sender = request.form.get('sender')

    if email not in inboxes:
        inboxes[email] = {
            'created_at': time.time(),
            'messages': []
        }

    inboxes[email]["messages"].append({
        "from": sender,
        "subject": subject,
        "body": body,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    })

    return "OK", 200

    session['email'] = generate_email()
    inboxes[session['email']] = {'created_at': time.time(), 'messages': []}
    threading.Thread(target=auto_delete_email, args=(session['email'],), daemon=True).start()
    return redirect('/email')

@app.route('/receive', methods=['POST'])
def receive_email():
    data = request.get_json()
    to = data.get('to')
    if to in inboxes:
        inboxes[to]['messages'].append({
            'from': data.get('from'),
            'subject': data.get('subject'),
            'body': data.get('body'),
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        })
        return jsonify({'status': 'received'})
    return jsonify({'status': 'Email not found'}), 404

@app.route('/messages')
def get_messages():
    email = session.get('email')
    if email and email in inboxes:
        return jsonify(inboxes[email]['messages'])
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
