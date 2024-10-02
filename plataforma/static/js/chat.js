document.addEventListener('DOMContentLoaded', eventos)

function eventos() {
    let input_ideia = document.getElementsByClassName('input-ideia')[0]
    let input_submit = document.getElementsByClassName('input-submit')[0]
    input_ideia.addEventListener("input", (event) => {
        texto = event.target
        if(texto.value.trim() == '') {
            input_submit.style = 'background-color: #F8F9FA;'
        } else {
            input_submit.style = 'background-color: #9BF6FF;'
        }
    })
    carregarMensagem()
}

function carregarMensagem() {
    let btn_submit = document.getElementsByClassName('input-submit')[0]
    console.log(btn_submit)
    btn_submit.addEventListener('click', () => {
        let container = document.getElementsByClassName('apresentacao-chat')[0]
        let msgInicial = document.getElementsByClassName('apresentacao-chat-msg')[0]
        let input_ideia = document.getElementsByClassName('input-ideia')[0]
        let id_personagem = document.getElementById('id-personagem').innerText
        let img_personagem = document.querySelector('.persona-imagem-container > img').src
        
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

            let respUsuario = document.createElement('div')
            respUsuario.innerHTML = `
            <div class="mensagem-imagem">
                <img class="msg-img-personagem" src="asd" alt="Neymar">
            </div>
            <p class="carregando-resposta">Carregando...</p>
            `
            respUsuario.classList.add('mensagem-resposta')
            container.appendChild(respUsuario)

            src_img = document.getElementsByClassName('msg-img-personagem')
            for(var i = 0; i < src_img.length; i++) {
                src_img[i].src = img_personagem
            }

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
                    respUsuario.getElementsByClassName('carregando-resposta')[0].innerText = ''
                    respUsuario.innerHTML += `
                    <article>${result}</article>
                    `
                })

            input_ideia.value = ''
            btn_submit.style = 'background-color: #F8F9FA;'
            container.scrollTop = container.scrollHeight
        }
    })
}