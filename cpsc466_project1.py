from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
  
  
app = Flask(__name__)
  
  
app.secret_key = 'xyzsdfg'
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'userinfo'
  
mysql = MySQL(app)
  
@app.route('/')

#routes to the login page, user inputs email/password
@app.route('/login', methods =['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'
            return render_template('user.html', mesage = mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage = mesage)
  
 #allows user to logout 
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))
  
 # CREATE: allows the user to register
@app.route('/register', methods =['GET', 'POST'])
def register():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not userName or not password or not email:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO user VALUES (NULL, % s, % s, % s)', (userName, email, password, ))
            mysql.connection.commit()
            mesage = 'You have successfully registered !'
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('register.html', mesage = mesage)

# READ: list all users in the database
@app.route("/user", methods=["GET"])
def get_user():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    user = cur.fetchall()
    cur.close()
    return jsonify(user)

# UPDATE: update an existing user listing in the database based on provided ID
@app.route("/user/<int:user_userid>", methods=["PUT"])
def update_user(userid):
    userid = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    cur = mysql.connection.cursor()

    # check if the user with the given ID exists
    cur.execute("SELECT * FROM user WHERE id = %s", (user_userid,))
    existing_user = cur.fetchone()
    if not existing_user:
        cur.close()
        return jsonify({"message": "User not found"}), 404

    # update the user if it exists
    cur.execute(
        "UPDATE user SET name = %s, email = %s, password = %s WHERE userid = NULL",
        (name, email, password, userid),
    )
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Users updated successfully"}), 200
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)