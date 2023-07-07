const form = document.querySelector("form");
const email = document.getElementById("email");
const nombre = document.getElementById("nombre");
const password = document.getElementById("password");
const warnings = document.getElementById("warnings");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const emailIn = email.value.trim();
  const nombreIn = nombre.value.trim();
  const passwordIn = password.value.trim();

  if (!isValidEmail(emailIn)) {
    showWarning("El email no es válido");
    return;
  }

  if (document.fvalida.nombre.value.length==0){
    showWarning("Tiene que escribir su nombre");
    document.fvalida.nombre.trim()
    return;
}


  if (passwordIn.length < 8) {
    showWarning("La contraseña debe tener al menos 8 caracteres");
    return;
  }

     if (emailIn === "Juan.p@gmail.com" && nombreIn === "Juan Perez") {
        redirectTo("Usuario registrado success.html");

   } else if (emailIn === "seba.g@gmail.com" && nombreIn === "Seba Gajardo") {
        redirectTo("Usuario registrado success.html");

   } else {
       redirectTo("sesion iniciada log usurio.html");
       showSuccessMessage("Enviado");

}






});

function isValidEmail(emailIn) {
  const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
  return emailRegex.test(emailIn);
}

function showWarning(message) {
  warnings.innerHTML = message;
}

function showSuccessMessage(message) {
  warnings.innerHTML = message;
}

function redirectTo(url) {
  window.location.href = url;

}