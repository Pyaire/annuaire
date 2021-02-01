import mysql.connector as MC

nom="François"
prenom="Premier"
num=696969690

mydb = MC.connect(
    host="localhost",
    user="root",
    passwd="",
    database="annuaire"
)

mycursor = mydb.cursor()

sql_ajout= "select Nom,Prenom,Numero from num"
# test = (prenom,nom,num)

mycursor.execute(sql_ajout)

myreslut=mycursor.fetchall()

mydb.commit()

for result in myreslut:
    print(result)