from django.shortcuts import render, redirect, get_object_or_404
from tallerRayo.models import Atencion, formularioContacto, formularioRes
import pdb
from django.contrib.auth.decorators import login_required
from tallerRayo.forms import RegistroForm
from django.views.decorators.csrf import csrf_protect

from tallerRayo.utils.encriptacion import Encriptacion



def indexTallermlween(request):
    context={}
    return render(request, 'indexTallermlween.html', context)

def inicio_sesion_usuario(request):
    context = {}
    return render(request, 'inicio_sesion_usuario.html', context)

def inicio_sesion_mec_admi(request):
    context = {}
    return render(request, 'inicio_sesion_mec_admi.html', context)

def iniciar_session_como_mecanico(request):
    context = {}
    return render(request, 'iniciar_session_como_mecanico.html', context)

def registro_de_usuario(request):
    context = {}
    return render(request, 'registro_de_usuario.html', context)

def IniciarSesion_adr(request):
    context = {}
    return render(request, 'IniciarSesion_adr.html', context)

@login_required
def cuenta_angel_d_revilla(request):
    context = {}
    return render(request, 'cuenta_angel_d_revilla.html', context)

def formulario_atenciones_CORREGIDO(request):
    context = {}
    return render(request, 'formulario_atenciones_CORREGIDO.html', context)

def Ver_atenciones_por(request):
    context = {}
    return render(request, 'Ver_atenciones_por.html', context)

def Ver_atenciones_x_mecanico(request):
    context = {}
    return render(request, 'Ver_atenciones_x_mecanico.html', context)

def detalle_trabajo1_mecanica_makween_23(request, id):
    atencion = get_object_or_404(Atencion, trabajo=id)
    context = {'atencion': atencion}
    return render(request, 'detalle_trabajo1_mecanica_makween_23.html', context)

def detalle_trabajo2_makween_23(request):
    context = {}
    return render(request, 'detalle_trabajo2_makween_23.html', context)

def detalle_trabajo3_makween_23(request):
    context = {}
    return render(request, 'detalle_trabajo3_makween_23.html', context)

def Estado_antenciones_adr(request):
    formres= formularioRes.objects.all()
    context={"formres": formres}
    return render(request, 'Estado_antenciones_adr.html', context)

def atencion_añadida_success_gp(request):
    context = {}
    return render(request, 'atencion_añadida_success_gp.html', context)


def Estado_antenciones_gp(request):
    context = {}
    return render(request, 'Estado_antenciones_gp.html', context)

def Estado_antenciones_jg(request):
    context = {}
    return render(request, 'Estado_antenciones_jg.html', context)

def formulario_enviado_succes(request):
    context = {}
    return render(request, 'formulario_enviado_succes.html', context)


def Formulario_contacto(request):
    context = {}
    return render(request, 'Formulario_contacto.html', context)

def mantenciones_ingresadas_usuario(request):
    context = {}
    return render(request, 'mantenciones_ingresadas_usuario.html', context)

def nueva_atencion_añadida_success_adr(request):
    context = {}
    return render(request, 'nueva_atencion_añadida_success_adr.html', context)

def registro_existoso(request):
    context = {}
    return render(request, 'registro_existoso.html', context)

def ingresar_atenciones_carro(request):
    context = {}
    return render(request, 'ingresar_atenciones_carro.html', context)


@login_required
def menu(request):
    context={}
    if request.user.is_authenticated:
        request.session["usuario"]=request.user.username
        usuario=request.session["usuario"]
        context={'usuario':usuario}
    return render(request,'menu.html',context)

def listado_atenciones(request):
    atenciones = Atencion.objects.all()
    context={"atenciones": atenciones}
    return render(request, 'listado_atenciones.html', context)

def listado_atenciones_usuario(request):
    atenciones = Atencion.objects.all().order_by('nombreMecanico')

    context = {
        'atenciones': atenciones
    }

    return render(request, 'listado_atenciones_usuario.html', context)

def listado_atenciones_usuario2(request):
    atenciones = Atencion.objects.all().order_by('categoria')

    context = {
        'atenciones': atenciones
    }

    return render(request, 'listado_atenciones_usuario.html', context)
    
def modificar_atenciones(request, pk):
    context={"mensaje":"Atencion no encontrada"}
    if pk != "":
        atencion_obj =  Atencion.objects.get(trabajo=pk)
        atencion_obj.rutCliente = Encriptacion.decrypt(atencion_obj.rutCliente)
        if atencion_obj:
            context={"atencion":atencion_obj}
            return render(request, "formulario_atenciones_modificar.html", context)
    return render(request, 'listado_atenciones.html', context)

def eliminar_atenciones(request, pk):
    context={}
    try:
        obj = Atencion.objects.get(trabajo=pk)
        obj.delete()
        atenciones = Atencion.objects.all()
        context={"atenciones": atenciones, "mensaje":"Eliminado con exito"}
        return render(request, 'listado_atenciones.html', context)
    except:
        atenciones = Atencion.objects.all()
        context={"atenciones": atenciones, "mensaje":"Error al eliminar"}
        return render(request, 'listado_atenciones.html', context)

def update_atenciones(request):
    if request.method != "POST":
        context = {}
        return render(request, 'formulario_atenciones_modificar.html', context)
    else:
        if request.POST["aceptar-terminos"] == "on":
            try:
                obj = Atencion.objects.get(trabajo=request.POST["trabajo"])
                if obj:
                    cliente_obj = formularioContacto.objects.filter(nombreCliente = request.POST["nombreCliente"]).first()
                    if cliente_obj is None:
                        cliente_obj= formularioContacto(nombreCliente=request.POST["nombreCliente"])
                        cliente_obj.save()
                    obj.diagnostico=request.POST["diagnostico"]
                    obj.fecha=request.POST["fecha"]
                    obj.modeloAuto=request.POST["modeloAuto"]
                    obj.nombreMecanico=request.POST["nombreMecanico"]
                    obj.cliente=cliente_obj
                    obj.rutCliente=Encriptacion.encrypt(request.POST["rutCliente"])
                    obj.costo=request.POST["costo"]
                    obj.garantia=request.POST["garantia"]
                    obj.save()
                    atenciones = Atencion.objects.all()
                    context={'mensaje':"Se modifico con exito", "atenciones": atenciones}
                    return render(request, "listado_atenciones.html", context)
                else:
                    context={'mensaje':"Error al modificar atencion"}
                    return render(request, "formulario_atenciones_modificar.html", context)
            except:
                    atenciones = Atencion.objects.all()
                    context={"atenciones": atenciones, "mensaje":"Error al actualizar campo erroneo"}
                    return render(request, 'listado_atenciones.html', context)

def agregar_atenciones(request):
    # pdb.set_trace()
    if request.method != "POST":
        context = {}
        return render(request, 'formulario_atenciones_CORREGIDO.html', context)
    else:
        trabajo=request.POST["trabajo"]
        diagnostico=request.POST["diagnostico"]
        fecha=request.POST["fecha"]
        modeloAuto=request.POST["modeloAuto"]
        imagenAuto=""
        nombreMecanico=request.POST["nombreMecanico"]
        nombreCliente=request.POST["nombreCliente"]
        rutCliente=request.POST["rutCliente"]
        costo=request.POST["costo"]
        garantia=request.POST["garantia"]
        aceptar_terminos=request.POST["aceptar-terminos"]

        if aceptar_terminos == "on":
            try:
                cliente_obj = formularioContacto.objects.filter(nombreCliente = nombreCliente).first()
                if cliente_obj is None:
                    cliente_obj= formularioContacto(nombreCliente=nombreCliente)
                    cliente_obj.save()

                if cliente_obj:
                    obj = Atencion.objects.create(
                        trabajo = trabajo,
                        diagnostico = diagnostico,
                        fecha = fecha,
                        modeloAuto =  modeloAuto,
                        imagenAuto = imagenAuto,
                        nombreMecanico = nombreMecanico,
                        cliente = cliente_obj,
                        rutCliente = Encriptacion.encrypt(rutCliente),
                        costo = costo,
                        garantia = garantia,
                    )
                    obj.save()
                    if obj:
                        atenciones = Atencion.objects.all()
                        context={'mensaje':"Se agrego con exito", "atenciones": atenciones}
                        return render(request, "listado_atenciones.html", context)
                    else:
                        context={'mensaje':"Error al crear atencion"}
                        return render(request, "formulario_atenciones_CORREGIDO.html", context)
            except:
                atenciones = Atencion.objects.all()
                context={"atenciones": atenciones, "mensaje":"Error al guardar"}
                return render(request, 'listado_atenciones.html', context)
            

@csrf_protect
def registro_de_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.save()
                return redirect('registro_existoso')
            except Exception as e:
                print(str(e))
        else:
            print(form.errors)
    else:
        form = RegistroForm()

    return render(request, 'registro_de_usuario.html', {'form': form})

def ate_aprobada(request):
    if request.method != "POST":
        context = {}
        return render(request, 'formulario_res.html', context)
    else:
        trabajos = request.POST["contexto"]
        estado = request.POST["estadoAte"]
        tipoAtencion = request.POST["tipo"]
        diasHabiles = request.POST["dias"]
        justificacion = request.POST["justificacion"]

        try:
            formulario_res = formularioRes.objects.create(
                trabajos=trabajos,
                estado=estado,
                tipoAtencion=tipoAtencion,
                diasHabiles=diasHabiles,
                justificacion=justificacion
            )
            formulario_res.save()

            if formulario_res:
                return redirect('listado_atenciones') 
            else:
                context = {'mensaje': "Error al crear formularioRes"}
                return render(request, "formulario_res.html", context)
        except:
            formulario_res_list = formularioRes.objects.all()
            context = {
                'formulario_res_list': formulario_res_list,
                'mensaje': "Error al guardar"
            }
            return render(request, 'listado_atenciones.html', context)
        
def ate_rechazada(request):
    if request.method != "POST":
        context = {}
        return render(request, 'formulario_resS.html', context)
    else:
        trabajos = request.POST["contexto"]
        estado = request.POST["estadoAte"]
        tipoAtencion = request.POST["tipo"]
        diasHabiles = request.POST["dias"]
        justificacion = request.POST["justificacion"]

        try:
            formulario_res = formularioRes.objects.create(
                trabajos=trabajos,
                estado=estado,
                tipoAtencion=tipoAtencion,
                diasHabiles=diasHabiles,
                justificacion=justificacion
            )
            formulario_res.save()

            if formulario_res:
                return redirect('listado_atenciones') 
            else:
                context = {'mensaje': "Error al crear formularioRes"}
                return render(request, "formulario_resS.html", context)
        except:
            formulario_res_list = formularioRes.objects.all()
            context = {
                'formulario_res_list': formulario_res_list,
                'mensaje': "Error al guardar"
            }
            return render(request, 'listado_atenciones.html', context)
    
    
def modificar_atenciones_us(request, pk):
    context={"mensaje":"Atencion no encontrada"}
    if pk != "":
        atencion_obj =  Atencion.objects.get(trabajo=pk)
        atencion_obj.rutCliente = Encriptacion.decrypt(atencion_obj.rutCliente)
        if atencion_obj:
            context={"atencion":atencion_obj}
            return render(request, "formulario_atenciones_us.html", context)
    return render(request, 'listado_atenciones.html', context)

def update_atenciones_us(request):
    if request.method != "POST":
        context = {}
        return render(request, 'formulario_atenciones_us.html', context)
    else:
        if request.POST["aceptar-terminos"] == "on":
            try:
                obj = Atencion.objects.get(trabajo=request.POST["trabajo"])
                if obj:
                    cliente_obj = formularioContacto.objects.filter(nombreCliente = request.POST["nombreCliente"]).first()
                    if cliente_obj is None:
                        cliente_obj= formularioContacto(nombreCliente=request.POST["nombreCliente"])
                        cliente_obj.save()
                    obj.diagnostico=request.POST["diagnostico"]
                    obj.fecha=request.POST["fecha"]
                    obj.modeloAuto=request.POST["modeloAuto"]
                    obj.categoria=request.POST["categoria"]
                    obj.materiales=request.POST["materiales"]
                    obj.nombreMecanico=request.POST["nombreMecanico"]
                    obj.cliente=cliente_obj
                    obj.rutCliente=Encriptacion.encrypt(request.POST["rutCliente"])
                    obj.costo=request.POST["costo"]
                    obj.garantia=request.POST["garantia"]
                    obj.verify= "1"
                    obj.save()
                    atenciones = Atencion.objects.all()
                    context={'mensaje':"Se modifico con exito", "atenciones": atenciones}
                    return render(request, "listado_atenciones.html", context)
                else:
                    context={'mensaje':"Error al modificar atencion"}
                    return render(request, "formulario_atenciones_us.html", context)
            except:
                    atenciones = Atencion.objects.all()
                    context={"atenciones": atenciones, "mensaje":"Error al actualizar campo erroneo"}
                    return render(request, 'listado_atenciones.html', context)
            
def modificar_atenciones_usuario(request, pk):
    context={"mensaje":"Atencion no encontrada"}
    if pk != "":
        atencion_obj =  Atencion.objects.get(trabajo=pk)
        atencion_obj.rutCliente = Encriptacion.decrypt(atencion_obj.rutCliente)
        if atencion_obj:
            context={"atencion":atencion_obj}
            return render(request, "modificar_atenciones_usuario.html", context)
    return render(request, 'listado_atenciones_usuario.html', context)

def update_atenciones_usuario(request):
    if request.method != "POST":
        context = {}
        return render(request, 'modificar_atenciones_usuario.html', context)
    else:
        if request.POST.get("aceptar-terminos") == "on":
            try:
                obj = Atencion.objects.get(trabajo=request.POST["trabajo"])
                if obj:
                    cliente_obj = formularioContacto.objects.filter(nombreCliente=request.POST["nombreCliente"]).first()
                    if cliente_obj is None:
                        cliente_obj = formularioContacto(nombreCliente=request.POST["nombreCliente"])
                        cliente_obj.save()
                    obj.diagnostico = request.POST["diagnostico"]
                    obj.fecha = request.POST["fecha"]
                    obj.modeloAuto = request.POST["modeloAuto"]
                    obj.categoria = request.POST["categoria"]
                    obj.materiales = request.POST["materiales"]
                    obj.nombreMecanico = request.POST["nombreMecanico"]
                    obj.cliente = cliente_obj
                    obj.rutCliente = Encriptacion.encrypt(request.POST["rutCliente"])
                    obj.costo = request.POST["costo"]
                    obj.garantia = request.POST["garantia"]
                    obj.verify = "1"
                    obj.save()
                    atenciones = Atencion.objects.all()
                    context = {'mensaje': "Se modificó con éxito", "atenciones": atenciones}
                    return redirect("listado_atenciones_usuario", context)
                else:
                    context = {'mensaje': "Error al modificar atención"}
                    return render(request, "modificar_atenciones_usuario.html", context)
            except:
                atenciones = Atencion.objects.all()
                context = {"atenciones": atenciones, "mensaje": "Error al actualizar campo erroneo"}
                return render(request, 'listado_atenciones_usuario.html', context)

def eliminar_atenciones_usuario(request, pk):
    context={}
    try:
        obj = Atencion.objects.get(trabajo=pk)
        obj.delete()
        atenciones = Atencion.objects.all()
        context={"atenciones": atenciones, "mensaje":"Eliminado con exito"}
        return render(request, 'listado_atenciones_usuario.html', context)
    except:
        atenciones = Atencion.objects.all()
        context={"atenciones": atenciones, "mensaje":"Error al eliminar"}
        return render(request, 'listado_atenciones_usuario.html', context)


from django.urls import reverse

def buscar_atencion(request):
    if request.method == 'POST':
        busqueda = request.POST.get('busquedadeatencion')
        try:
            atencion = Atencion.objects.get(trabajo=busqueda)
            return redirect(reverse('detalle_trabajo1_mecanica_makween_23', kwargs={'id': atencion.trabajo}))
        except Atencion.DoesNotExist:
            mensaje = 'No se encontró ninguna atención con ese trabajo.'
            return render(request, 'indexTallermlween.html', {'mensaje': mensaje})
    else:
        return render(request, 'indexTallermlween.html')
    
def detalle_trabajo_ultima_fecha(request):
    atencion = Atencion.objects.order_by('-fecha').first()
    context = {'atencion': atencion}
    return render(request, 'detalle_trabajo1_mecanica_makween_23.html', context)

def detalle_trabajo_ultima_fecha2(request):
    atencion = Atencion.objects.order_by('-fecha').all().values('trabajo')[1]
    return redirect('detalle_trabajo1_mecanica_makween_23', id=atencion['trabajo'])

def detalle_trabajo_ultima_fecha3(request):
    atencion = Atencion.objects.order_by('-fecha').all().values('trabajo')[2]
    return redirect('detalle_trabajo1_mecanica_makween_23', id=atencion['trabajo'])
