from flask import Flask, render_template, request, session, jsonify, redirect
import random, string, time, threading
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'

inboxes = {}

# توليد إيميل وهمي
def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = 'fakelymail.com'
    return f'{username}@{domain}'

# حذف تلقائي بعد وقت محدد
def auto_delete_email(email, lifetime=1800):
    time.sleep(lifetime)
    inboxes.pop(email, None)

@app.route('/')
def home():
    return render_template('home.html')  # تأكد فعلاً أن الملف اسمه كذا

@app.route('/email')
def index():
    email = generate_email()
    session['email'] = email

    if email not in inboxes:
        inboxes[email] = {
            'created_at': time.time(),
            'messages': []
        }
        threading.Thread(target=auto_delete_email, args=(email,), daemon=True).start()

    remaining = int(inboxes[email]['created_at'] + 1800 - time.time())
    return render_template('index.html', email=email, timer=remaining)

@app.route("/blog1")
def blog1():
    return render_template("blog1.html")

@app.route("/blog2")
def blog2():
    return render_template("blog2.html")

@app.route('/change')
def change_email():
    session['email'] = generate_random_email()
    return '', 204

@app.route('/messages')
def get_messages():
    email = session.get('email')
    if email and email in inboxes:
        return jsonify(inboxes[email]['messages'])
    return jsonify([])

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/receive', methods=['POST'])
def receive_email():
    from datetime import datetime
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

from flask import send_from_directory

@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml')

@app.route('/ads.txt')
def ads():
    return app.send_static_file('ads.txt')

@app.route('/googleddb8bfe162a125fe.html')
def google_verify():
    return send_from_directory('static', 'googleddb8bfe162a125fe.html')
    
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)