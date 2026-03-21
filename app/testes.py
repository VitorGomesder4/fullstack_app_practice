from utils.save_env import save_env
from dotenv import load_dotenv
import os
print(os.getcwd())

load_dotenv("backend/.env")

x = os.getenv("var_teste")

x = int(x)
print(f"chegou como {x}")

x += 1

y = str(x)
print(type(x))

r = save_env("var_teste", y)
print(r)

if r == True:
    print(f"saiu como {x}")