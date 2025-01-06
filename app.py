from flask import Flask, render_template, request
from dotenv import load_dotenv#cargar variables de entorno
from pymongo import MongoClient#para usar la base de datos
import os#para ibtener las variables de entorno con getenv
import datetime

fecha=datetime.datetime.today().strftime('%d-%m-%Y')
print(fecha)


load_dotenv()
app=Flask(__name__)#iniciamos la app con flask

cliente=MongoClient(os.getenv('endpoint'))#cliente del mongodb
app.db=cliente.blogs#la base de datos del cliente, en este caso blogs

entradas=[entrada for entrada in app.db.entradas.find({})]#este es el array que tendrá las entradas de la bd


@app.route('/',methods=['GET','POST'])
def mostrar_form():
    titulo=''
    contenido=''

    if request.method=='POST':
        titulo=request.form.get('titulo').strip()
        contenido=request.form.get('contenido').strip()
        parametros={'title':titulo,'content':contenido}
        entradas.append(parametros)
        app.db.entradas.insert_one(parametros)

    return render_template('blog.html',entradas=entradas,fecha=fecha)
if __name__=='__main__':
    app.run(debug=True)