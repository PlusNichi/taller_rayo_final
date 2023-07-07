document.getElementById("#").addEventListener("submit", function(event) {
    var nombreComp = document.getElementById("nombreComp").value;
    var correoGmail = document.getElementById("correoGmail").value;
    var marca = document.getElementById("marca").value;
    var modeloAuto = document.getElementById("modeloAuto").value;
    var tipoServicio = document.getElementById("tipoServicio").value;
    var descripcion = document.getElementById("descripcion").value;

    
    
    
  
    if (nombreComp === "" || correoGmail === "" || marca === "" || modeloAuto === "" || tipoServicio === "" || descripcion === "" ) {
      event.preventDefault(); // Evita el envío del formulario

    
        
  
      // Muestra el mensaje de error
      alert("Por favor, completa todos los campos del formulario.");
    }  
  });