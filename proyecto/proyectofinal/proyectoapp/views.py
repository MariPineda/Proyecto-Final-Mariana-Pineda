from django.shortcuts import render

from django.http import HttpResponse
from proyectoapp.models import Socios, Libros, Avatar
from proyectoapp.forms import SociosFormulario, LibrosFormulario, BusquedaSocios, UserRegistrationForm, UserEditForm, AvatarFormulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):

    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user.id)
        return render(request, 'index.html', {'url': avatar[0].image.url})
    
    return render(request, 'index.html')
    
    #formulario = BusquedaSocios()
    #return render(request, 'busqueda_socios.html', {"formulario" : formulario})

def socios(request):

    return render(request, 'socios.html')

def libros(request):

    return render(request, 'libros.html')


def about_me(request):

    return render(request, 'about.html')


def admin(request):

    return render(request, 'admin.html')
    

def socios_formulario(request):

    if request.method == "POST":
        formulario = SociosFormulario(request.POST)
        print("is valid: {formulario.is_valid}")
        if formulario.is_valid():
            datos = formulario.cleaned_data
            nombre = datos.get("nombre")
            apellido = datos.get("apellido")
            email = datos.get("email")
            socio = datos.get("socio")
            activo = datos.get("activo")

            socios = Socios(nombre=nombre, apellido=apellido, email=email, socio=socio, activo=activo)
            socios.save()
            return render(request, 'index.html')
        
    else:
        formulario = SociosFormulario()
        return render(request, 'socios_formulario.html', {"formulario": formulario})
    
    
def libros_formulario(request):

    if request.method == "POST":
        formulario = LibrosFormulario(request.POST)
        print("is valid: {formulario.is_valid}")
        if formulario.is_valid():
            datos = formulario.cleaned_data
            titulo = datos.get("titulo")
            tipo = datos.get("tipo")
            edadRecomendada = datos.get("edadRecomendada")

            libros = Libros(titulo=titulo, tipo=tipo, edadRecomendada=edadRecomendada)
            libros.save()
            return render(request, 'index.html')
        
    else:
        formulario = LibrosFormulario()
        return render(request, 'libros_formulario.html', {"formulario": formulario})


def busqueda_socios(request):
    
    if request.method == "GET":
        
        socio = request.GET.get("socio")

        if socio is None:
            return HttpResponse("Debe enviar un socio")
        
        socio = Socios.objects.filter(socio=socio)
        
        return render(request, 'busqueda_socios_respuesta.html', {"socio": socio})
        
        
def buscar_socios(request):

    if request.method == "GET":
        
        socio = request.GET.get("socio")
      
        if socio is None:
            return HttpResponse("Enviar el socio a buscar")
        socio= Socios.objects.filter(socio__icontains=socio)
        #print(socio)
        #return HttpResponse(f"Se buscó el socio número: {socio}")

        return render (request,'busqueda.html', {"socio" : socio})
    

def listar_libros(request):
    libros = Libros.objects.all()
    contexto = {"libros" : libros}
    return render(request, 'listar_libros.html', contexto)

def eliminar_libros(request, nombre_libro):

    libro = Libros.objects.get(titulo=nombre_libro)

    libro.delete()

    libros = Libros.objects.all()
    contexto = {"libros": libros}
    
    return render(request, 'listar_libros.html', contexto)

def editar_libros(request, nombre_libro):

    libro = Libros.objects.get(titulo=nombre_libro)

    if request.method == "POST":

        formulario = LibrosFormulario(request.POST)

        if formulario.is_valid():

            datos_libro = formulario.cleaned_data

            libro.titulo = datos_libro.get("titulo")
            libro.tipo = datos_libro.get("tipo")
            libro.edadRecomendada = datos_libro.get("edadRecomendada")

            libro.save()

            return render(request, 'index.html')

    formulario = LibrosFormulario(initial={"titulo": libro.titulo, "tipo": libro.tipo, "edadRecomendada": libro.edadRecomendada})

    return render(request, 'editar_libros.html', {"formulario": formulario, "libro_nombre": nombre_libro})

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:

                login(request,user)

                return render(request, 'index.html', {"mensaje": f"Bienvenido {username}"})
            
            else:

                return render(request, 'index.html', {"mensaje": f"Usuario o contraseña inválidos"})
            
        else:
            return render(request, 'index.html', {"mensaje": f"Datos incorrectos"})

    form = AuthenticationForm
    return render(request, 'login.html', {"form" : form})

def registrar(request):

    if request.method == "POST":

        #form = UserCreationForm(request.POST)

        form = UserRegistrationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get("username")

            form.save()

            return render(request, 'index.html', {"mensaje": f"Se dio de alta el usuario {username}"})


    #form = UserCreationForm()
    form = UserRegistrationForm()

    return render(request,'registro.html', {"form": form})

@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == "POST":

        formulario = UserEditForm(request.POST)

        if formulario.is_valid():

            informacion = formulario.cleaned_data

            usuario.email = informacion.get("email")
            usuario.password1 = informacion.get("password1")
            usuario.password2 = informacion.get("password2")
            usuario.last_name = informacion.get("last_name")
            usuario.first_name = informacion.get("first_name")

            usuario.save()

            return render(request, 'index.html')
    
    else:
        
        formulario = UserEditForm(initial={"email": usuario.email })
        
        return render(request, 'editar_usuario.html', {"formulario": formulario})
    
@login_required
def avatar(request):

    if request.method == "POST":
        
        formulario = AvatarFormulario(request.POST, request.FILES)

        if formulario.is_valid():

            user = User.objects.get(username=request.user)
            avatar = Avatar(user=user, image=formulario.cleaned_data.get("image"))
            avatar.save()

            return render(request, 'index.html')
        
        
    formulario = AvatarFormulario()

    return render(request, 'avatar.html', {"formulario": formulario})

#Vistas basadas en clases
class SociosList(ListView):

    model = Socios
    template_name = 'socios_list.html'

class SociosDetalle(DetailView):

    model = Socios
    template_name = 'socios_detalle.html'

class SociosCreacion(CreateView):

    model = Socios
    fields = ['nombre', 'apellido', 'email', 'socio', 'activo']
    template_name = 'socios_form.html'
    success_url = "/proyecto-app/socios/list"

class SociosUpdate(UpdateView):

    model = Socios
    fields = ['nombre', 'apellido', 'email', 'socio', 'activo']
    template_name = 'socios_form.html'
    success_url = "/proyecto-app/socios/list"

class SociosDelete(DeleteView):

    model = Socios
    template_name = 'socios_confirm_delete.html'
    success_url = "/proyecto-app/socios/list"

