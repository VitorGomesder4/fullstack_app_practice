from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from models.curso import Curso
from models.aluno import ALUNO
from utils.save_env import save_env
import mysql.connector
import re
import os
import time
import datetime as dt

#Loading .env file and creating environment variables
load_dotenv(".env")

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")

#Creating database connection
db = mysql.connector.connect(host = DB_HOST, user = DB_USER, password = DB_PASSWORD, database = DB_DATABASE)

#Instantiating the flask app
app = Flask(__name__)

lista_cursos_objects = []
lista_alunos_objects = []

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/cursos", methods=["GET"])
def exibir_cursos():
    return render_template("cursos.html")

@app.route("/alunos", methods=["GET"])
def exibir_alunos():
    return render_template("registrar_alunos.html")

@app.route("/alunos/registrar_aluno", methods=['POST'])
def registrar_aluno():
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

    if not data or not campos_obrigatorios.issubset(data.keys()):
        return jsonify({"message": "error data required"}), 400

    for chave in data:

        ealpha_numerico = re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$", data[chave])

        if chave == "dt_nascimento" and data[chave]:
            pass

        elif not data[chave]:
            data[chave] = None
            continue
            
        data[chave] = data[chave].strip()

        if chave == "sg_sexo":
            if len(data[chave]) != 1 or data[chave].lower() not in ["m", "f"]:
                data[chave] = None

        elif chave == "co_estadocivil":
            if len(data[chave]) != 1 or data[chave] not in ['1', '2', '3', '4', '5']:
                data[chave] = None

        elif chave == "nome":
            if len(data[chave]) > 20 or not ealpha_numerico:
                data[chave] = None
        
        elif chave == "no_pai" or chave == "no_mae":
            if len(data[chave]) > 70 or not ealpha_numerico:
                data[chave] = None
            
    """    
    new_aluno = ALUNO(
        data["dt_nascimento"], #datetime
        data["sg_sexo"], #size_limit of 1 char
        data["nome"], #size_limit of 20 char
        data["co_estadocivil"], #size_limit of 1 char
        data["no_pai"], #size_limit of 70 char
        data["no_mae"] #size_limit of 70 char
        )

    lista_alunos_objetcts.append(new_aluno)
    """

    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO ALUNO (DT_NASCIMENTO, SG_SEXO, NOME, CO_ESTADOCIVIL, NO_PAI, NO_MAE) VALUES (%s, %s, %s, %s, %s, %s)",
        (data['dt_nascimento'], data['sg_sexo'], data['nome'], data['co_estadocivil'], data['no_pai'], data['no_mae'])
        )
    db.commit()

    return jsonify({"message": "Aluno registrado com sucesso!"}), 200


@app.route("/cursos/registrar", methods=["POST"])
def registrar_curso():
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
        nome = data["nome_do_curso_key"]
    )
    lista_cursos_objects.append(new_curso)
    """

    cursor = db.cursor()

    cursor.execute("INSERT INTO CURSO (NOME) VALUES (%s)", (data['nome_do_curso_key'],))
    db.commit()

    return jsonify({"message": f"Curso {data['nome_do_curso_key']} registrado com sucesso!"})
    

if __name__ == "__main__":
    app.run(debug=True)