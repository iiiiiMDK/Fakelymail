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

@app.route('/mesothelioma-legal-help')
def blog11():
    return render_template('mesothelioma-legal-help.html')

@app.route('/structured-settlements')
def blog12():
    return render_template('structured-settlements.html')

@app.route('/credit-card-processing')
def blog13():
    return render_template('credit-card-processing.html')

@app.route('/cybersecurity-small-business')
def blog14():
    return render_template('cybersecurity-small-business.html')

@app.route('/digital-marketing-strategies')
def blog15():
    return render_template('digital-marketing-strategies.html')

@app.route('/privacy-tips')
def blog1():
    return render_template('privacy-tips.html')

@app.route('/email-tricks')
def blog2():
    return render_template('email-tricks.html')

@app.route('/disposable-emails-benefits')
def blog3():
    return render_template('disposable-emails-benefits.html')

@app.route('/stay-safe-online')
def blog4():
    return render_template('stay-safe-online.html')

@app.route('/email-privacy-101')
def blog5():
    return render_template('email-privacy-101.html')

@app.route('/guard-your-inbox-tips')
def blog6():
    return render_template('guard-your-inbox-tips.html')

@app.route('/real-email-risks')
def blog7():
    return render_template('real-email-risks.html')

@app.route('/avoid-shopping-spam')
def blog8():
    return render_template('avoid-shopping-spam.html')

@app.route('/why-use-fakelymail')
def blog9():
    return render_template('why-use-fakelymail.html')

@app.route('/protect-identity-online')
def blog10():
    return render_template('protect-identity-online.html')

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