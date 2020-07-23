from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from miFormularioApp.forms import MiFormulario
# Create your views here.

def holaMundo(request):
    return HttpResponse("Hola mundo")


def holaMundoTemplate(request):
    nombre = 'Agustin'
    diccionario = {'nombre': nombre}
    return render (request, "HolaMundo/holaMundo.html", diccionario)


def home(request):
    # Si estamos identificados vamos a la home
    if request.user.is_authenticated:
        return render(request, "Principal/home.html")
    # En otro caso redireccionamos al index
    return redirect('/index/')

def index(request):
    print ("entre al index")
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "Principal/index.html", {'form': form})


def registro(request):
    # Creamos el formulario de autenticación vacío
    form = MiFormulario()
    print ("hola")
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = MiFormulario(request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')


    # Si queremos borramos los campos de ayuda
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

    # Si llegamos al final renderizamos el formulario
    return render(request, "Principal/registro.html", {'form': form})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
