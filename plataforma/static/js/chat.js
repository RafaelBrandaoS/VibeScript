document.addEventListener('DOMContentLoaded', eventos)

function eventos() {
    let input_ideia = document.getElementsByClassName('input-ideia')[0]
    let input_submit = document.getElementsByClassName('input-submit')[0]
    let estaVazio = true
    input_ideia.addEventListener("input", (event) => {
        texto = event.target
        if(texto.value.trim() == '') {
            input_submit.style = 'background-color: #F8F9FA;'
            estaVazio = true
        } else {
            input_submit.style = 'background-color: #9BF6FF;'
            estaVazio = false
        }
    })
    carregarMensagem(estaVazio)
}

function carregarMensagem(estaVazio) {
    let btn_submit = document.getElementsByClassName('input-submit')[0]
    console.log(btn_submit)
    btn_submit.addEventListener('click', () => {
        console.log("CLICOOOOUUU!!!!")
        let container = document.getElementsByClassName('apresentacao-chat')[0]
        let msgInicial = document.getElementsByClassName('apresentacao-chat-msg')[0]
        let input_ideia = document.getElementsByClassName('input-ideia')[0]
        let id_personagem = document.getElementById('id-personagem').innerText
        
        if (input_ideia.value != '') {

            msgInicial.style = 'display: none;'
            
            let mensagens = document.createElement('div')
            mensagens.innerHTML = ''
            mensagens.classList.add('mensagens')
            container.appendChild(mensagens)
    
            let msgUsuario = document.createElement('div')
            msgUsuario.innerHTML = `<p>${input_ideia.value}</p>`
            msgUsuario.classList.add('mensagem-usuario')
            mensagens.appendChild(msgUsuario)
    
            fetch(`resposta/${id_personagem}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(input_ideia.value)
            })
                .then(response => response.text())
                .then(result => {
                    console.log(result)
                    let respUsuario = document.createElement('div')
                    respUsuario.innerHTML = `
                    <div class="mensagem-resposta">
                        <img src="" alt="Neymar">
                    </div>
                    <p>${result}</p>
                    `
                    respUsuario.classList.add('mensagem-usuario')
                    container.appendChild(respUsuario)
                })

            input_ideia.value = ''
        }
    })
}