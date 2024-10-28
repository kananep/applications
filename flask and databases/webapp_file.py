from flask import Flask, render_template , request ,send_file
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy import func
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5000/height_collator'

db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__= 'data'
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)
    
    def __init__(self, email_ , height_):
        self.email_ = email_
        self.height_ = height_
    
# Define a function to create the tables
def create_tables():
    with app.app_context():
        db.create_all()   

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success',methods=['POST'])

def success():
    global file
    if request.method == 'POST':
        file = request.files['file']
        file.save(secure_filename('Uploaded_' + file.filename))
        with open('Uploaded_' + file.filename , 'w') as new_file:
            new_file.write('This was added later!')
        
        print(file)
        print(type(file))
        return render_template('index.html' , btn = 'download.html')
    
    
@app.route('/download')
def download():
    return send_file('Uploaded_' + file.filename ,attachment_filename = 'yourFile.csv' , as_attachment=True)

    

if __name__ == '__main__':
    app.debug = True
    app.run(port=3600)