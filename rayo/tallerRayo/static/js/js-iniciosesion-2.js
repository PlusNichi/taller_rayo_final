const $formulario = document.querySelector("#formulario")
      $email = document.querySelector("email")
      $password = document.querySelector("contraseña")

$formulario.onsubmit = evento =>{
    evento.preventDefault();
    const email = email.value
         password = password.value

         //validar
    if(email.endsWith("@hotmail.com")){
      alert("No puede ser hotmail");
      return;
    
    }

      if(password.value.length <8){
        warnings += 'La constraseña no es valida <br>'
        entrar = true
    }
    $formulario.submit();
    
    


}