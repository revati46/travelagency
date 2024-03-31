from flask import Flask, render_template , redirect ,session ,request
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

app.secret_key = 'secret_key'

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

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/explore")
def explore():
    return render_template('explore.html')

if __name__ == '__main__':
    app.run(debug=True)