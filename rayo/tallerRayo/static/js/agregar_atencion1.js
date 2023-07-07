const carro = new Carrito();
const carrito = document.getElementById('carrito');
const atencion= document.getElementById('lista-productos');
const listaAtencion = document.querySelector('#lista-carrito tbody');
const vaciarCarritoBtn = document.getElementById('vaciar_carrito');
const procesarPedidoBtn = document.getElementById('procesar_pedido');
cargarEventos();

function cargarEventos(){
    atencion.addEventListener('click', (e)=>{carro.agregarAtencion(e)});

    carrito.addEventListener('click', (e)=>{carro.eliminarAtencion(e)});

    vaciarCarritoBtn.addEventListener('click', (e)=>{carro.vaciarCarrito(e)});

}
