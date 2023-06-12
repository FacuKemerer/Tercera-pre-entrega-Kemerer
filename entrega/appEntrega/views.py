from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import cliente_form, auto_form, historia_form, buscar_auto
from .models import Cliente, Auto, HistorialTrabajos

def inicio(request):
    return render(request, "appEntrega/index.html")

def servicio(request):
    return render(request, "appEntrega/servicio.html")

def horarios(request):
    return render(request, "appEntrega/horarios.html")

def agregar_cliente(request):
    if request.method == "POST":
        miFormulario = cliente_form(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cliente = Cliente(nombre=informacion["nombre"],
                            apellido=informacion["apellido"], 
                            telefono=informacion["telefono"]
                            )
            cliente.save()
            return render(request, "appEntrega/confirmacion.html")
    else:
        miFormulario = cliente_form()
    return render(request, "appEntrega/form_cliente.html", {"miFormulario": miFormulario})

def agregar_auto(request):
    if request.method == "POST":
        formulario = auto_form(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            nombre_cliente = informacion["nombre_cliente"]
            apellido_cliente = informacion["apellido_cliente"]
            cliente = Cliente.objects.get(nombre=nombre_cliente, apellido=apellido_cliente)
            auto = Auto(cliente=cliente,
                        patente=informacion["patente"].upper(),
                        )
            auto.save()
            return render(request, "appEntrega/confirmacion.html")
    else:
        formulario = auto_form()
    return render(request, "appEntrega/form_auto.html", {"formulario": formulario})

def agregar_historia(request):
    if request.method == "POST":
        form_hist = historia_form(request.POST)
        if form_hist.is_valid():
            informacion = form_hist.cleaned_data
            patente = informacion["patente"]
            auto = Auto.objects.get(patente=patente)
            historial = HistorialTrabajos(auto=auto,
                                        descripcion=informacion["descripcion"])
            historial.save()
            return render(request, "appEntrega/confirmacion.html")
    else:
        form_hist = historia_form()
    return render(request, "appEntrega/form_hist.html", {"form_hist": form_hist})

def busqueda_auto(request):
    if request.method == 'POST':
        form = buscar_auto(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            autos = Auto.objects.filter(patente__icontains=informacion["patente"])
            resultados = []
            for auto in autos:
                cliente = auto.cliente
                trabajos = HistorialTrabajos.objects.filter(auto=auto)
                resultados.append({'auto': auto, 'cliente': cliente, 'trabajos': trabajos})
            return render(request, "appEntrega/lista.html", {"resultados": resultados})
    else:
        form = buscar_auto()
    return render(request, 'appEntrega/buscar_form.html', {'form': form})


