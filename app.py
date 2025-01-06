from flask import Flask, render_template, request
from dotenv import load_dotenv#cargar variables de entorno
from pymongo import MongoClient#para usar la base de datos
import os#para ibtener las variables de entorno con getenv

load_dotenv()
app=Flask(__name__)#iniciamos la app con flask

cliente=MongoClient(os.getenv('endpoint'))#cliente del mongodb
app.db=cliente.blogs#la base de datos del cliente, en este caso blogs




if __name__=='__main__':
    app.run(debug=True)