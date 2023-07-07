
document.getElementById("miFormulario").addEventListener("submit", function(event) {
  var fecha = document.getElementById("fecha").value;
  var imagenAuto = document.getElementById("imagen-auto").value;
  var nombrePersona = document.getElementById("nombre-persona").value;
  var rut = document.getElementById("rut").value;
  var nombre = document.getElementById("nombre").value;
  var diagnostico = document.getElementById("diagnostico").value;
  var costo = document.getElementById("costo").value;
  var garantia = document.getElementById("garantia").value;
  var aceptarTerminos = document.getElementById("aceptar-terminos").checked;

  if (fecha === "" || imagenAuto === "" || nombrePersona === "" || rut === "" || nombre === "" || diagnostico === "" || costo === "" || garantia === "" || !aceptarTerminos) {
    event.preventDefault(); // Evita el envío del formulario

    // Muestra el mensaje de error
    alert("Por favor, completa todos los campos del formulario.");
  }

  
  
});
