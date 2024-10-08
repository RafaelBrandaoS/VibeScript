document.addEventListener('DOMContentLoaded', eventos)

function eventos() {
    let btnsSenha = document.getElementsByClassName('verSenha')
    for(let i = 0; i < btnsSenha.length; i++) {
        btnsSenha[i].addEventListener('click', (event) => {
            let container = event.target.parentElement
            let inputSenha = container.querySelector('input')
            let btn = container.querySelector('.verSenha')

            if(inputSenha.type == 'password') {
                btn.classList.replace('bi-eye-fill', 'bi-eye-slash-fill')
                inputSenha.setAttribute('type', 'text')
            } else {
                if(inputSenha.type == 'text') {
                    inputSenha.setAttribute('type', 'password')
                    btn.classList.replace('bi-eye-slash-fill', 'bi-eye-fill')
                }
            }

        })
    }
}