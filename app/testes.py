from dotenv import load_dotenv
import os

load_dotenv("app/.env")

cursos_id_control = os.getenv("cursos_id_control")
alunos_id_control = os.getenv("alunos_id_control")

print(cursos_id_control)

"""
string = " vitor "
string = string.strip()

print(f"a{string}a")
"""

"""dicionario = {"teste": "  valor  ", "teste2": "  valor2  "}

for chave in dicionario.keys():
    print(f"{chave}: {dicionario[chave]} =>", end= " ")
    dicionario[chave] = dicionario[chave].strip()
    print(f"{chave}: {dicionario[chave]}")"""

"""
dicionario = {"sg_sexo": None}

if dicionario["sg_sexo"]: if has value
    print(True)
else:
    print(False) :if not value
"""

"""dicionario = {"sg_sexo": False}

for chave in dicionario:
    if chave == "sg_sexo" and not dicionario[chave]:
        print("a")

string = "abcdê"
print(string.isalpha())"""