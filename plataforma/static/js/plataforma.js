document.addEventListener('DOMContentLoaded', eventos)

function eventos() {
    let personagens = document.getElementsByClassName('personagem')
    for (let i = 0; i < personagens.length; i++) {
        personagens[i].addEventListener('click', () => {
            let id_personagem = personagens[i].getElementsByClassName('id-personagem')[0].innerText
            escolha_personagem(id_personagem)
        }) 
    }
}

function escolha_personagem(id_personagem) {
    console.log(id_personagem)
    window.location.href = `/plataforma/chat/${id_personagem}`
}

