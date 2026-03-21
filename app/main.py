from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from models.curso import Curso
from utils.save_env import save_env
import mysql.connector
import os
import time

#Loading .env file and creating environment variables
load_dotenv(".env")

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")

cursos_id_control = os.getenv("cursos_id_control")

cursos_id_control = int(cursos_id_control)

print(type(cursos_id_control))

#Creating database connection
db = mysql.connector.connect(host = DB_HOST, user = DB_USER, password = DB_PASSWORD, database = DB_DATABASE)

#Instantiating the flask app
app = Flask(__name__)

lista_cursos_objects = []

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/cursos", methods=["GET"])
def exibir_cursos():
    return render_template("cursos.html")

@app.route("/cursos/registrar", methods=["POST"])
def registrar_curso():
    global cursos_id_control
    """ TABLE CURSO:
        CO_CURSO INTEGER PRIMARY KEY
        NOME CHAR(40) NULL
    """

    data = request.get_json()

    if not data or 'nome_do_curso_key' not in data:
        return jsonify({"message": "error no data or data key"}), 400

    new_curso = Curso(
        CO_CURSO = cursos_id_control,
        NOME = data["nome_do_curso_key"]
    )

    lista_cursos_objects.append(new_curso)

    cursor = db.cursor()

    cursor.execute("INSERT INTO CURSO (CO_CURSO, NOME) VALUES (%s, %s)", (cursos_id_control, data['nome_do_curso_key']))
    db.commit()

    cursos_id_control += 1

    save_env("cursos_id_control", cursos_id_control)

    return jsonify({"message": f"Curso {data['nome_do_curso_key']} registrado com sucesso!"})
    

if __name__ == "__main__":
    app.run(debug=True)