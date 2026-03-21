function registrar_novo_curso(nomedocurso){
    fetch("/cursos/registrar", { /* Enviando uma requisição para registrar um curso novo */
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({nome_do_curso_key: nomedocurso})
    }
    )
    .then(response => response.json())
    .then(data => {console.log(data)})
    .catch(error => {console.log('Ocorreu um erro: ', error)})
};