const form = document.getElementById("form")
const email = document.getElementById("email")
const password = document.getElementById("contraseña")


form.addEventListener("submit", e=>{
    e.preventDefault()
    let warnings = ""
    let entrar = false
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/
    parrafo.innerHTML = ""
    
    if(!regexEmail.test(email.value)){
        warnings += 'El email no es valido <br>'
        entrar = true

    }
    if(password.value.length <8){
        warnings += 'La constraseña no es valida <br>'
        entrar = true
    }
    if(entrar){
        parrafo.innerHTML = warnings
    }else{
        parrafo.innerHTML = "Enviado"
    }
})



