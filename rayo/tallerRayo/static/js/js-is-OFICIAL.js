const form = document.querySelector("form");
const email = document.getElementById("email");
const password = document.getElementById("password");
const warnings = document.getElementById("warnings");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const emailIn = email.value.trim();
  const passwordIn = password.value.trim();

  if (!isValidEmail(emailIn)) {
    showWarning("El email no es válido");
    return;
  }

  if (passwordIn.length < 8) {
    showWarning("La contraseña debe tener al menos 8 caracteres");
    return;
  }

  if (emailIn === "angelrevilla@gmail.com") {
    redirectTo("menu");
  } else if (emailIn === "javiergonzales@gmail.com") {
    redirectTo("sesion iniciada log 2");
  } else if (emailIn === "gonzalopenaloza@gmail.com") {
    redirectTo("sesion iniciada log 3");
  } else {
    redirectTo("");
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