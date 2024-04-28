from flask import Flask, render_template , request ,send_file
import pandas as pd
from geopy.geocoders import ArcGIS
import datetime

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5000/geocode'

# db = SQLAlchemy(app)

# class geo_code(db.Model):
#     __tablename__= 'data'
#     id = db.Column(db.Integer, primary_key=True)
#     address__ = db.Column(db.String(120), unique=True)
#     name__ = db.Column(db.String(120))
#     employees__ = db.Column(db.Integer)
#     latitude_ = db.Column(db.Float)
#     longitude_ = db.Column(db.Float)
    
    
#     def __init__(self, address__ , name__ , employees__ ):
#         self.address__ = address__
#         self.name__  = name__ 
#         self.employees__ = employees__
#         self.latitude_ = latitude_
#         self.longitude_ = longitude_
    
# Define a function to create the tables
# def create_tables():
#     with app.app_context():
#         db.create_all() 
        

@app.route('/')
def index():
    return render_template('index.html')        
          
        
@app.route('/success_table',methods=['POST'])

def success_table():
    if request.method == 'POST':    
        file = request.files['file']
        try:
            df = pd.read_csv(file)
            gc=ArcGIS(scheme='http')
            df['cordinate'] = df.Address.apply(gc.geocode)
            df['latitude']  = df.cordinate.apply(lambda x: x.latitude if x != None else None)
            df['longitude']  = df.cordinate.apply(lambda x: x.longitude if x != None else None)
            df = df.drop('cordinate',1)
            filename=datetime.datetime.now().strftime("sample_files/%Y-%m-%d-%H-%M-%S-%f"+".csv")
            df.to_csv(filename,index=None)
            return render_template('success_table.html' ,text = df.to_html(), btn = 'download.html' )     
        except Exception as e:
            return render_template("index.html", text=str(e))
    

@app.route("/download/")
def download():
    return send_file('uploads/geocoded.csv' ,attachment_filename = 'yourFile.csv' , as_attachment=True)
    
if __name__ == '__main__':
    app.debug = True
    app.run(port=1600)    