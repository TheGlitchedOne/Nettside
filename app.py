from flask import Flask, render_template, url_for, request  # importing necessary modules from the Flask framework for web application development
import sqlite3 as sql                                       # importing the sqlite3 module for database operations
from werkzeug.security import check_password_hash           # checks if the provided password matches the stored hash
from werkzeug.security import generate_password_hash        # generates a hashed password for secure storage in the database
import os                                                   # importing the os module to access environment variables for configuration
#PEPPER = os.environ.get("PASSWORD_PEPPER")# gets the PEPPER from environment variable
PEPPER = "Pas5word" # This should match your SECRET_KEY #!swap with line above or use a diffrrent seluson when website is active, and remove this line 
app = Flask(__name__)

# Set the secret key once
print("\033[93m" +"starting app")
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'dev-key-only')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enternew')
def new_login():
    return render_template('login.html')

""" the function below handles adding new users"""
@app.route('/enternew', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        msg = ""
        try:
            nm = request.form['username']       #gets the username from the user has entered
            pin = request.form['pasword']       #gets the password from the user has entered
            hashed_pw = generate_password_hash(pin + PEPPER)    # Hash the password
         #add the user to the database
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO login (username, pasword) VALUES (?,?)", (nm, hashed_pw))
                con.commit()
                msg = "Record successfully added"
        except Exception as e:
            msg = f"Error in insert operation: {e}"
        return render_template("result.html", msg=msg) # Redirect to result page to show status

    return render_template('login.html')

""" the function below handles login and Hash the password whide adding the PEPPER for extra security 
if the database gets compromised or anyone looks at the database, they will not see the actual password just garbage data"""
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
            USERNAME = request.form['username']
            PASSWORD_INPUT = request.form['pasword']

            with sql.connect("database.db") as con:
                con.row_factory = sql.Row
                cur = con.cursor()
                cur.execute("SELECT * FROM login WHERE username=?", (USERNAME,))
                user_record = cur.fetchone()
                

                if user_record:
                    stored_hash = user_record['pasword']

                    if user_record and check_password_hash(user_record['pasword'], PASSWORD_INPUT + PEPPER):
                        # Read role from database
                        IS_IT = user_record['is_IT']  # assuming it’s "true" or "false" as string
                        
                        if IS_IT in ["true", "1", "yes"]:
                            return render_template("IT.html", msg="Welcome IT Staff! You have access to the admin panel.")
                        else:
                            return render_template("result.html", alert_msg="Welcome Regular User!")
                    
                
                # If login fails
                return render_template("index.html",
                                       alert_msg="Invalid username or password")

        except Exception as e:  # if something goes wrong it give an error message
            print(e)
            return render_template("index.html",
                                   alert_msg="Login error")

    return render_template("index.html")
        
        # Return moved outside of 'finally' to avoid SyntaxWarning

@app.route('/submit_ticket', methods=['POST']) # handle the page after login
def submit_ticket():
    if request.method == 'POST':
        msg = ""
        try:
            PROBLEM_TYPE = request.form.get('problem_type')
            PRIORITY = request.form.get('priority')
            SUBJECT = request.form.get('subject')
            EXTRA_INFO = request.form.get('extra_info')
            ATTACHMENT = request.files.get('attachment')
            ATTACHMENT_FILENAME = ATTACHMENT.filename
            ATTACHMENT_TYPE = ATTACHMENT.content_type

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO problem (problem_type, proiority, subject, extra_info, attachment_data, attachment_filename, attachment_type) VALUES (?,?,?,?,?,?,?)", (PROBLEM_TYPE, PRIORITY, SUBJECT, EXTRA_INFO, ATTACHMENT.read(), ATTACHMENT_FILENAME, ATTACHMENT_TYPE))
                con.commit()
                msg = "Record successfully added"
        except Exception as e:
            msg = f"Error in insert operation: {e}"
        return render_template("result.html", msg=msg) # Redirect to result page to show status

    # Handle ticket submission logic here
    return render_template("result.html", msg="Ticket submitted successfully")


@app.route('/IT') #! not in use yet
def IT(): 
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from problem")
    rows = cur.fetchall()
    con.close()
    return render_template('IT.html', rows=rows)

if __name__ == "__main__":
    app.run(debug=True)