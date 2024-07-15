from flask import Flask, render_template, request, redirect, url_for, session 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/eduguide'
db = SQLAlchemy(app)

#Capital c is there in class contacts beacuase small is there in database contacts table
class Contacts(db.Model):
    #sno,name,email,phone_number,msg,date
    sno = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)
    msg = db.Column(db.String(300), unique=False, nullable=False)
    date = db.Column(db.String(12),  nullable=True)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/subjects")
def subjects():
    return render_template('subjects.html')

@app.route("/contact", methods = ['GET', 'POST'])   #it should be methods
def contact():
    if(request.method=='POST'):
        
        #(fetched from database)
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        #add entry to the databse
        entry = Contacts(name=name,email=email,phone_number=phone,msg=message,date=datetime.now())

        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html')


#after all the process of db connection add action to the html(contact.html) file form tag


@app.route("/science")
def science():
    return render_template('science.html')

@app.route("/science1")
def science1():
    return render_template('science1.html')

@app.route("/science2")
def science2():
    return render_template('science2.html')

@app.route("/science3")
def science3():
    return render_template('science3.html')

@app.route("/science4")
def science4():
    return render_template('science4.html')

@app.route("/science5")
def science5():
    return render_template('science5.html')

@app.route("/science6")
def science6():
    return render_template('science6.html')

@app.route("/science7")
def science7():
    return render_template('science7.html')

@app.route("/science8")
def science8():
    return render_template('science8.html')


@app.route("/science9")
def science9():
    return render_template('science9.html')

@app.route("/science10")
def science10():
    return render_template('science10.html')

@app.route("/science11")
def science11():
    return render_template('science11.html')

@app.route("/science12")
def science12():
    return render_template('science12.html')

@app.route("/science13")
def science13():
    return render_template('science13.html')

@app.route("/science14")
def science14():
    return render_template('science14.html')

@app.route("/science15")
def science15():
    return render_template('science15.html')

@app.route("/science16")
def science16():
    return render_template('science16.html')


if __name__ == '__main__':
    app.run(debug=True)
