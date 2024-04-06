from flask import Flask, render_template , redirect ,session , request, jsonify
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import openai
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_BINDS'] = {'feedback': 'sqlite:///feedback.db'}
db = SQLAlchemy(app)

app.secret_key = 'secret_key'

openai.api_key = os.environ.get("OPENAI_API_KEY")

class User(db.Model):
    id = db.Column( db.Integer , primary_key=True )
    email = db.Column( db.String(50) , nullable = False ,unique =True)
    number = db.Column( db.String(10) , nullable = False ,unique =True )
    password = db.Column(db.String(40), nullable=False)
    
    def __init__(self,email,number,password):
        self.email = email
        self.number = number
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') 
        
    def check_password(self ,password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    
with app.app_context():
    db.create_all()    
    
    
    
    
class Feedback(db.Model):
    __bind_key__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    mobilenumber = db.Column(db.String(10), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __init__(self,firstname,lastname,email,mobilenumber,message):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.mobilenumber = mobilenumber
        self.message = message

with app.app_context():
    db.create_all()
        
        
@app.route("/contact", methods=['POST', 'GET'])
def submit_feedback():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        mobilenumber = request.form['mobilenumber']
        message = request.form['message']
        
        if not firstname:
            return render_template('contact.html', error='Firstname cannot be empty')
        
        feedback = Feedback(firstname=firstname, lastname=lastname, email=email, mobilenumber=mobilenumber, message=message)
        db.session.add(feedback)
        db.session.commit()
        return redirect('/dashboard')
    else:
        return render_template('contact.html')
  

@app.route("/register", methods=['GET' , 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        number = request.form['mobileno'] 
        new_user = User(email=email , password=password , number=number )
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    else:
        return render_template('register.html')
    
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session['email'] = user.email
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Invalid User')

    return render_template('login.html')
   
@app.route('/dashboard')
def dashboard():
    if 'email' in session:  
        user = User.query.filter_by(email=session['email']).first()  
        return render_template('dashboard.html', user=user)
    else:
        return redirect('/login')  
    
  
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/explore")
def explore():
    return render_template('explore.html')

@app.route("/ai")
def ai():
    return render_template('ai.html')

@app.route("/generate-trip", methods=['POST'])
def generate_text():
    data = request.json
    budget = request.form['budget']
    interests = request.form['interests']
    duration = request.form['duration']
    location = request.form['location']
    prompt = data.get("prompt")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    generated_text = response.choices[0].text.strip()
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(debug=True)