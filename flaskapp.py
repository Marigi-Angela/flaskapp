#FLASK APPLICATION

from flask import Flask , render_template, url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
db = SQLAlchemy(app)

class ContactDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname= db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return '<ContactDetails %r>' % self.id

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        message = request.form.get('message')
        new_contact = ContactDetails(email=email,firstname=firstname,lastname=lastname,message=message)

        #commit data to database
        db.session.add(new_contact) 
        db.session.commit()
        
        return redirect(url_for('home'))

    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)

# To execute, run the file. Then go to 127.0.0.1:5000 in your browser and look at a welcoming message.