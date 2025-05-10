from flask import Flask, render_template, request, session, jsonify, redirect, send_from_directory
import random, string, time, threading
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

inboxes = {}

# توليد إيميل وهمي
def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = 'fakelymail.com'
    return f'{username}@{domain}'

# حذف تلقائي بعد وقت
def auto_delete_email(email, lifetime=1800):
    time.sleep(lifetime)
    inboxes.pop(email, None)

# الصفحة الرئيسية
@app.route('/')
def home():
    return render_template('home.html')

# صفحة البريد المؤقت
@app.route('/email', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        custom = request.form.get('custom_name')
        if custom:
            username = ''.join(filter(str.isalnum, custom.strip()))
        else:
            username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    else:
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

    domain = 'fakelymail.com'
    email = f'{username}@{domain}'
    session['email'] = email

    if email not in inboxes:
        inboxes[email] = {
            'created_at': time.time(),
            'messages': []
        }
        threading.Thread(target=auto_delete_email, args=(email,), daemon=True).start()

    remaining = int(inboxes[email]['created_at'] + 1800 - time.time())
    return render_template('index.html', email=email, timer=remaining)


# صفحات البلوق
@app.route('/blog1')
def blog1():
    return render_template('blog1.html')

@app.route('/blog2')
def blog2():
    return render_template('blog2.html')

@app.route('/blog3')
def blog3():
    return render_template('blog3.html')

@app.route('/blog4')
def blog4():
    return render_template('blog4.html')

@app.route('/blog5')
def blog5():
    return render_template('blog5.html')

@app.route('/blog6')
def blog6():
    return render_template('blog6.html')

@app.route('/blog7')
def blog7():
    return render_template('blog7.html')

@app.route('/blog8')
def blog8():
    return render_template('blog8.html')

@app.route('/blog9')
def blog9():
    return render_template('blog9.html')

@app.route('/blog10')
def blog10():
    return render_template('blog10.html')

# تغيير الإيميل
@app.route('/change')
def change_email():
    session['email'] = generate_email()
    return '', 204

# جلب الرسائل
@app.route('/messages')
def get_messages():
    email = session.get('email')
    if email and email in inboxes:
        return jsonify(inboxes[email]['messages'])
    return jsonify([])

# سياسة الخصوصية والتواصل
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# استقبال الرسائل من Mailgun
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

# ملفات السيو و التحقق
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

# تشغيل التطبيق
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)