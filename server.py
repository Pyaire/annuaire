from flask import Flask, render_template, request
import mysql.connector as MC

app = Flask(__name__)

mydb = MC.connect(
     host="localhost",
     user="root",
     passwd="",
     database="annuaire"
 )

mycursor = mydb.cursor()


######################################################################################################

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/resultat',methods = ['POST'])
def resultat():
  result = request.form
  n = result['nom']
  sql_recherche= "select nom,prenom,numero from num"

  mycursor.execute(sql_recherche)

  mydb.commit()

  myresult=mycursor.fetchall()

  return render_template("resultat.html", nom=n)

@app.route('/ajout',methods = ['post'])
def ajout():
  return render_template('ajout.html')

@app.route('/recherche',methods = ['post'])
def recherche():
  return render_template('recherche.html')

@app.route('/retour',methods = ['post'])
def retour():
  result = request.form
  n = result['nom']
  p = result['prenom']
  num = result['numero']
  
  sql_ajout= "insert into num (Prenom,Nom,Numero) values (%s, %s,%s)"
  test = (p,n,num)

  mycursor.execute(sql_ajout,test)

  mydb.commit()
  return render_template('retour.html')

app.run(debug=True)

