from flask import Flask, render_template
import json
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from flask import request

app = Flask(__name__, static_folder = "static")
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///correction.sqlite3'
db = SQLAlchemy(app)

db.init_app(app)


class Example(db.Model):
    id = db.Column( db.Integer, primary_key = True)
    title=db.Column(db.String(100))
    txt=db.Column(db.String(200))
    iscorrect=db.Column(db.Boolean,default=True,nullable=False)
    corrections=db.relationship('Correction',backref='example')
    def __repr__(self):
        return f'<Example "self.title">'
class Correction(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    id1 = db.Column( db.Integer)
    time=db.Column(db.String(100))
    txt=db.Column(db.String(200))
    Correct=db.Column(db.Boolean,default=True,nullable=False)
    eg_id=db.Column(db.Integer,db.ForeignKey('example.id'))
    def __repr__(self):
        return f'<Correction "{self.time}" "{self.Correct}">'

txt="स्लॅमडान्स एकोणीशे सत्याऐंशी ह्या आधुनिक न्वार चित्रपटाचा कला दिग्दर्शक युगेनियो झारेटी म्हणतो न्वारचे आकर्षण कालातीत आहे कारण न्वारच्या नायकाला सुटकेचा मार्ग नसतो पर्याय नसतात"
splttxt=txt.split(" ")
print(len(splttxt))
tseries=['0.42', '1.12', '1.81', '2.37', '2.91', '3.28', '3.76', '4.41', '4.82', '5.49', '6.29', '6.73', '7.11', '7.85', '8.58', '8.94', '9.22', '9.81', '10.48', '10.98', '11.74', '12.17', '12.49', '12.6']
print(len(tseries))


details = {
    'TimeSeries' : tseries,
    'Subtitle' : splttxt,
    
}
det=pd.DataFrame(details)



@app.route("/updatedcorrection/<int:id>",methods=['POST'])
def updatedb(id):
    if request.method=='POST':
        dat=request.get_json()
        egz=Example.query.get_or_404(id)
        for correction in egz.corrections:
            if correction.id1 in dat['name']:
                print(correction.id1)
                correction.Correct=False
            else:
                correction.Correct=True
            db.session.add(correction)
            db.session.commit()
        return "<p>Success</p>"

@app.route("/")
def viewexample():
    egz=Example.query.all()
    return render_template('viewexample.html',egz=egz)


@app.route("/viewexamples/<int:idd>",methods=["GET"])
def viewexamples(idd):
    egz=Example.query.get_or_404(idd)
    egz.iscorrect=False
    db.session.add(egz)
    db.session.commit()
    jsonA=[]
    corray=[]
    for correction in egz.corrections:
        jsonA.append(correction.time)
        if correction.Correct==False:
            corray.append(correction.id1)
    df1={
        "TimeSeries":jsonA
    }
    df2={
        "corray":corray
    }
    jso=pd.DataFrame(df1)
    cor=pd.DataFrame(df2)
        
    return render_template("newview.html",egz=egz,jsonobject=jso.to_json(),corObj=cor.to_json())






if __name__ == '__main__':
    app.run(debug = True)

