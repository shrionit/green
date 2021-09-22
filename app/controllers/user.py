import hashlib
from flask import flash, render_template
from app.models.user import User
from app.utils.dbbase import Session, Base, engine
from markupsafe import escape

Base.metadata.create_all(engine)

session = Session()

class UserController:
    
    def hashIt(self, text):
        return hashlib.md5(text.encode()).hexdigest()
    
    def login(self, req):
        
        notify = None
        
        if req.method == 'POST':
            email = escape(str(req.form['email']))
            password = escape(str(req.form['password']))
            password = self.hashIt(password)

            query_results = session.query(User).filter(User.email.in_([email]), User.password.in_([password]))
            
            result = query_results.first()
            
            notify = {}
            
            if result:
                # session['logged_in'] = True
                notify['type'] = "SUCCESS"
                notify['message'] = "Login Successful"
                notify['submsg'] = result
            else:
                notify['type'] = "ERROR"
                notify['message'] = "Login Failed"
                notify['submsg'] = "Incorrect email or password"

        return render_template("auth/login.html", notify=notify)
    
    def signup(self, req):
        
        notify = None

        if req.method == 'POST':
            name = escape(str(req.form['name']))
            email = escape(str(req.form['email']))
            password = escape(str(req.form['password']))
            query_results = session.query(User).filter(User.email.in_([email]))
            result = query_results.first()
            notify={}
            if not result:
                password = self.hashIt(password)
                user = User(name=name, email=email, password=password)
                session.add(user)
                session.commit()
                notify['message'] = "User registered successfully"
                notify['type'] = "SUCCESS"
            else:
                notify['message'] = "Email already exists"
                notify['type'] = "ERROR"

        return render_template("auth/signup.html", notify=notify)

user = UserController()
