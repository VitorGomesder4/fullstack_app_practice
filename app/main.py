from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from models.curso import Curso
from models.aluno import ALUNO
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
alunos_id_control = os.getenv("alunos_id_control")

cursos_id_control = str(cursos_id_control)

cursos_id_control = int(cursos_id_control)
alunos_id_control = int(alunos_id_control)

print(type(cursos_id_control))

#Creating database connection
db = mysql.connector.connect(host = DB_HOST, user = DB_USER, password = DB_PASSWORD, database = DB_DATABASE)

#Instantiating the flask app
app = Flask(__name__)

lista_cursos_objects = []
lista_alunos_objetcts = []

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/cursos", methods=["GET"])
def exibir_cursos():
    return render_template("cursos.html")

@app.route("/registrar_aluno")
def registrar_aluno():
    global alunos_id_control
    """ TABLE ALUNO:
        CO_ALUNO, DT_NASCIMENTO, SG_SEXO, NOME,       CO_ESTADOCIVIL, NO_PAI,     NO_MAE
        INT       DATETIME       CHAR(1)  VARCHAR(20) CHAR(1)         VARCHAR(70) VARCHAR(70)
    """

    data = request.get_json()

    campos_obrigatorios = {
        "dt_nascimento",
        "sg_sexo",
        "nome",
        "co_estadocivil",
        "no_pai",
        "no_mae"
        }

    if not data or not campos_obrigatorios.issubset(data.keys):
        return jsonify({"message": "error data required"}), 400

    for chave in data:
        if chave == "dt_nascimento":
            continue

        elif not data[chave]:
            data[chave] = "NULL"
            
        data[chave] = data[chave].strip()

        if chave == "sg_sexo":
            if len(data[chave]) != 1 or data[chave].lower() not in ["m", "f"]:
                data[chave] = "NULL"

        elif chave == "co_estadocivil":
            if len(data[chave]) != 1 or data[chave] not in ['1', '2', '3', '4', '5', '6']:
                data[chave] = "NULL"

        elif chave == "nome":
            if len(data[chave]) > 20 or not data[chave].isalpha():
                data[chave] = "NULL"
        
        elif chave == "no_pai" or "no_mae":
            if len(data[chave]) > 70 or not data[chave].isalpha():
                data[chave] = "NULL"
            
        
    new_aluno = ALUNO(
        alunos_id_control, 
        data["dt_nascimeto"], #datetime
        data["sg_sexo"], #size_limit of 1 char
        data["nome"], #size_limit of 20 char
        data["co_estadocivil"], #size_limit of 1 char
        data["no_pai"], #size_limit of 70 char
        data["no_mae"] #size_limit of 70 char
        )

    lista_alunos_objetcts.append(new_aluno)

    cursor = db.cursor()

    cursor.execute("INSERT INTO ALUNO (CO_ALUNO, DT_NASCIMENTO) VALUES (%s, %s)", (alunos_id_control, data['dt_nascimeto']))
    db.commit()

    alunos_id_control += 1

    save_env("alunos_id_control", alunos_id_control)


@app.route("/cursos/registrar", methods=["POST"])
def registrar_curso():
    global cursos_id_control
    """ TABLE CURSO:
        CO_CURSO INTEGER PRIMARY KEY
        NOME CHAR(40) NULL
    """

    data = request.get_json()

    campos_obrigatorios = {
        "nome_do_curso_key"
        }

    if not data or not campos_obrigatorios.issubset(data.keys()):
        return jsonify({"message": "error no data or data key"}), 404

    for chave in data:
        if chave == "nome_do_curso_key" and not data[chave].isalpha():
            return jsonify({"message": "data needs to do be alphanumeric"}), 400

    """
    new_curso = Curso(
        co_curso = cursos_id_control,
        nome = data["nome_do_curso_key"]
    )
    lista_cursos_objects.append(new_curso)
    """

    cursor = db.cursor()

    cursor.execute("INSERT INTO CURSO (NOME) VALUES (%s)", (data['nome_do_curso_key'],))
    db.commit()

    cursos_id_control += 1

    save_env("cursos_id_control", cursos_id_control)

    return jsonify({"message": f"Curso {data['nome_do_curso_key']} registrado com sucesso!"})
    

if __name__ == "__main__":
    app.run(debug=True)