from flask import Flask, render_template, request
import sqlite3
import smtplib
def send_email(to_email, chocolate):
    sender_email = "fadihafra@gmail.com"
    password = "wzgdbjpkagsroiey"

    message = f"Subject: Chocolate Order\n\nYou ordered {chocolate}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, to_email, message)
    server.quit()

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('chocolates.db')
    conn = sqlite3.connect('chocolates.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS orders
                 (id INTEGER PRIMARY KEY,
                  name TEXT,
                  email TEXT,
                  chocolate TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    name = request.form['name']          # ✅ ADD THIS
    email = request.form['email']
    chocolate = request.form['chocolate']

    conn = sqlite3.connect('chocolates.db')
    c = conn.cursor()

    c.execute(
        "INSERT INTO orders (name,email,chocolate) VALUES (?,?,?)",
        (name, email, chocolate)
    )

    conn.commit()
    conn.close()

    try:
        send_email(email, chocolate)
    except:
        print("Email not sent (server restriction)")

    return "Order placed successfully!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)