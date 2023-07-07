class Carrito{
    agregarAtencion(e){
        e.preventDefault();
        if(e.target.classList.contains('agregar-carrito')){
            const atencion = e.target.parentElement.parentElement;
            this.leerDatosAtencion(atencion);

            //console.log(atencion);
        }
    }
    leerDatosAtencion(atencion){
        const infoAtencion = {
            imagen: atencion.querySelector('img').src,
            precio: atencion.querySelector('.precio span').textContent,
            nombre: atencion.querySelector('h3').textContent,
            Tipo_mantencion: atencion.querySelector('h4').textContent,
            // ingreso: atencion.querySelector('p').textContent,
            dias_resolucion: atencion.querySelector('h5').textContent,
            id : atencion.querySelector('a').getAttribute('data-id'),
            cantidad: 1
        }
        this.insertarCarrito(infoAtencion);

    }

    insertarCarrito(atencion){
        const row = document.createElement('tr');
        // <td>${atencion.ingreso}</td>
        row.innerHTML = `
        <td>
            <img src="${atencion.imagen}" width=100>
        </td>
        <td>${atencion.precio}</td>
        <td>${atencion.nombre}</td>
        <td>${atencion.Tipo_mantencion}</td>
        <td>${atencion.dias_resolucion}</td>
        <td>
            <a href="#" class="borrar-producto fas fa-times-circle" data-id="${atencion.id}"></a>
        </td>
    `;
    listaAtencion.appendChild(row);
    // this.guardarProductosLocalStorage(producto);
    }

    eliminarAtencion(e){
        e.preventDefault();
        let atencion, atencionID;
        if(e.target.classList.contains('borrar-atencion')){
            e.target.parentElement.parentElement.remove();
            atencion = e.target.parentElement.parentElement;
            atencionID = atencion.querySelector('a').getAttribute('data-id');
        }
        // this.eliminarProductoLocalStorage(atencionID);
        // this.calcularTotal();

    }

    vaciarCarrito(e){
        e.preventDefault();
        while(listaAtencion.firstChild){
            listaAtencion.removeChild(listaAtencion.firstChild);
        }
        // this.vaciarLocalStorage();

        return false;

    }
}