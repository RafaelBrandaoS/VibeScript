document.addEventListener('DOMContentLoaded', eventos)

function eventos() {
    const btn_menu_lateral = document.getElementById('btn-menu-lateral')
    const menu_lateral = document.getElementsByClassName('infos-personagem')[0]
    const seta = document.querySelector('#btn-menu-lateral > span')
    btn_menu_lateral.addEventListener('click', () => {
        if(menu_lateral.classList.contains('infos-personagem-mostrar')) {
            menu_lateral.classList.remove('infos-personagem-mostrar')
            seta.innerText = 'arrow_forward_ios'
            document.getElementsByClassName('nome-img-persona')[0].style = 'box-shadow: none;'
            document.getElementsByClassName('data-hora-roteiro')[0].style = 'color: transparent;'
        } else {
            menu_lateral.classList.add('infos-personagem-mostrar')
            seta.innerText = 'arrow_back_ios'
            document.getElementsByClassName('nome-img-persona')[0].style = 'box-shadow: -2px 2px 3px #5b5b5b86;'
            document.getElementsByClassName('data-hora-roteiro')[0].style = 'color: black;'
        }
    })

    let input_ideia = document.getElementsByClassName('input-ideia')[0]
    let input_submit = document.getElementsByClassName('input-submit')[0]
    input_ideia.addEventListener("input", (event) => {
        texto = event.target
        menu_lateral.classList.remove('infos-personagem-mostrar')
        seta.innerText = 'arrow_forward_ios'
        document.getElementsByClassName('nome-img-persona')[0].style = 'box-shadow: none;'
        document.getElementsByClassName('data-hora-roteiro')[0].style = 'color: transparent;'
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
    let container = document.getElementsByClassName('apresentacao-chat')[0]
    let msgInicial = document.getElementsByClassName('apresentacao-chat-msg')[0]
    let input_ideia = document.getElementsByClassName('input-ideia')[0]
    let id_personagem = document.getElementById('id-personagem').innerText
    let img_personagem = document.querySelector('.persona-imagem-container > img').src

    function req_resposta() {
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
    }}

    btn_submit.addEventListener('click', req_resposta)
    input_ideia.addEventListener('keydown', (event) => {
        if(event.key === 'Enter') {
            req_resposta()
        }
    })
}