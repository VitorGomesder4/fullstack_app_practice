function registrar_novo_professor(sg_sexo = "", nome = "", dt_nascimento = ""){
    console.log({
        sg_sexo,
        nome,
        dt_nascimento
    })
    fetch("/professores/registrar_professor", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({sg_sexo, nome, dt_nascimento})
    }
    )
    .then(response => response.json())
    .then(data => {console.log(data)})
    .catch(error => {console.log('Ocorreu um erro: ', error)})
}