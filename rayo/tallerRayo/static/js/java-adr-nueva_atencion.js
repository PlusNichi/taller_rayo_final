document.getElementById("lario2").addEventListener("submit", function(event) {
    var trabajo = document.getElementById("txtTrabajo").value;
    var diagnostico = document.getElementById("txtDiagnostico").value;
    var imagenModelo = document.getElementById("imgImagen_modelo").value;
    var modeloVehiculo = document.getElementById("txtModelo_vehiculo").value;
    var fechaAtencion = document.getElementById("txtFecha_atencion").value;
    var costo = document.getElementById("txtcosto").value;
    var categoria = document.getElementById("txtCategoria").value;
    var materialesUtilizados = document.getElementById("txtMateriales_utilizados").value;
    var mecanico = document.getElementById("txtMecanico").value;
    var rutmecanico = document.getElementById("txtRut_mecanico").value;
    var nombrePropietario = document.getElementById("txtNombre_propietario").value;
    var rutPropietario = document.getElementById("txtRut_propietario").value;
    var garantia = document.getElementById("txtGarantia").value;
    var tipoServicio = document.getElementById("txtRut_propietario").value;
    
    //var fecha = document.getElementById("fecha").value;
    //var imagenAuto = document.getElementById("imagen-auto").value;
    //var nombrePersona = document.getElementById("nombre-persona").value;
    //var rut = document.getElementById("rut").value;
    //var nombre = document.getElementById("nombre").value;
    //var costo = document.getElementById("costo").value;
    //var garantia = document.getElementById("garantia").value;
    //var aceptarTerminos = document.getElementById("aceptar-terminos").checked;
  
    if (trabajo === "" || diagnostico === "" || imagenModelo === "" || modeloVehiculo === "" || fechaAtencion === "" || costo === "" || categoria === "" || garantia === "" || materialesUtilizados === "" || mecanico === "" || rutmecanico === "" || nombrePropietario === "" || rutPropietario === "" || garantia === "" || tipoServicio === "" || !aceptarTerminos) {
      event.preventDefault(); // Evita el envío del formulario
  
      // Muestra el mensaje de error
      alert("Por favor, completa todos los campos del formulario.");
    }
  });
  