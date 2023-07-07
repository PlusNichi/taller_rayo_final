const nombre = document.getElementById('nombre')
const password = document.getElementById('password')
const form = document.getElementById('form')
const errorElement = document.getElementById('error')

form.addEventListener('submit', (e) => {
  let messages = []
  if (nombre.value === '' || nombre.value == null) {
    messages.push('Se requiere poner el nombre')
  }

  if (password.value.length <= 6) {
    messages.push('La constraseña debe tener mas de 6 caracteres')
  }

  if (password.value.length >= 20) {
    messages.push('La contraseña debe tener menos de 20 caracteres')
  }

  if (password.value === 'password') {
    messages.push('Password cannot be password')
  }

  if (messages.length > 0) {
    e.preventDefault()
    errorElement.innerText = messages.join(', ')
  }
})