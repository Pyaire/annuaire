#ce programme n'est qu'un test et ne concerne pas le projet même
import mysql.connector as MC

nom="Ansel"
prenom="Premier"
num=696969690

mydb = MC.connect(
    host="localhost",
    user="root",
    passwd="",
    database="annuaire"
)

mycursor = mydb.cursor()

sql_ajout= "select Prenom,Nom,Numero from num where nom= %s"
test=(nom, )

mycursor.execute(sql_ajout,test)

myreslut=mycursor.fetchall()

mydb.commit()

for result in myreslut:
    print(result)
