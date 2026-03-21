from pathlib import Path

path_env_file = ".env"

#func update var values in .env
def save_env(var_name:str, var_value):
    env_path = Path(path_env_file)
    var_value = str(var_value)

    linhas = env_path.read_text().splitlines()
    encontrou = False

    for i, linha in enumerate(linhas):
        if linha.startswith("#") or "=" not in linha:
            continue
        nome, _ = linha.split("=", 1)
        if nome.strip() == var_name:
            linhas[i] = f"{var_name}={var_value}"
            encontrou = True
            break

    if not encontrou:
        linhas.append(f"{var_name}={var_value}")
        return False

    env_path.write_text("\n".join(linhas) + "\n")
    return True