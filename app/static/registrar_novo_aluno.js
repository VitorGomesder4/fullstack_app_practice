function registrar_novo_aluno(dt_nascimento = "", sg_sexo = "", nome = "", co_estadocivil = "", no_pai = "", no_mae = ""){
    console.log({
        dt_nascimento,
        sg_sexo,
        nome,
        co_estadocivil,
        no_pai,
        no_mae
    })
    fetch("/alunos/registrar_aluno", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({dt_nascimento, sg_sexo, nome, co_estadocivil, no_pai, no_mae})
    }
    )
    .then(response => response.json())
    .then(data => {console.log(data)})
    .catch(error => {console.log('Ocorreu um erro: ', error)})
}