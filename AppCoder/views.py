import email
from django.shortcuts import render
from django.urls import reverse_lazy
from AppCoder.models import Curso, Estudiante, Profesor
from django.http import HttpResponse
from AppCoder.forms import CursoForm, ProfeForm, UserRegisterForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.


def curso(self):
    
    curso= Curso(nombre="Django", comision=939393)
    curso.save()
    texto= f"Curso creado: {curso.nombre} {curso.comision}"
    return HttpResponse(texto)

def inicio(request):
    return render (request, "Appcoder/inicio.html")


def cursos(request):
    return render (request, "Appcoder/cursos.html")

@login_required
def profesores(request):
    return render (request, "Appcoder/profesores.html")

def estudiantes(request):
    return render (request, "Appcoder/estudiantes.html")

def entregables(request):
    return render (request, "Appcoder/entregables.html")


@login_required
def cursoFormulario(request): 
   
    '''if (request.method == "POST"):
        nombre = request.POST.get("curso")
        comision = request.POST.get("comision")
        curso=Curso(nombre=nombre, comision=comision)
        curso.save()
        return render (request, "AppCoder/inicio.html")
    
    return render(request, "Appcoder/cursoFormulario.html")
'''
    if (request.method=="POST"):
        form=CursoForm(request.POST)
        
        if form.is_valid():
            info=form.cleaned_data
            
            nombre=info["nombre"]
            comision=info["comision"]
            curso=Curso(nombre=nombre, comision=comision)
            curso.save()
            return render (request, "Appcoder/inicio.html")    
    else:
        form=CursoForm()
    return render (request, "Appcoder/cursoFormulario.html", {"formulario": form})



@login_required    
def profeFormulario(request):
    
    if request.method=='POST':
        form = ProfeForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            profesion=info["profesion"]
            profe=Profesor(nombre= nombre, apellido=apellido, email=email, profesion= profesion)
            profe.save()
            return render (request, "Appcoder/inicio.html")
    else:
        form=ProfeForm()        
    return render (request, "Appcoder/profeForm.html", {"formulario": form})


def busquedaComision(request):
    return render (request, "Appcoder/busquedaComision.html")

def buscar(request):
    if request.GET["comision"]:
        comi=request.GET["comision"]
        cursos=Curso.objects.filter(comision=comi)
        return render (request, "Appcoder/resultadosBusqueda.html", {"cursos":cursos})
    else:
        return render(request, "Appcoder/busquedaComision.html", {"error": "No se ingreso ninguna comision" })

def leerProfesores(request):
    profesores = Profesor.objects.all()
    return render (request, "Appcoder/leerProfesores.html", {"profesores": profesores} )

def eliminarProfesor(request, nombre_profesor): 
    profe = Profesor.objects.get(nombre=nombre_profesor)
    profe.delete()

    profesores = Profesor.objects.all()
    return render (request, "Appcoder/leerProfesores.html", {"profesores": profesores} )

@login_required
def editarProfesor(request, nombre_profesor):
    profe = Profesor.objects.get(nombre=nombre_profesor)
    if request.method=="POST":
        form=ProfeForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            profe.nombre=info["nombre"]
            profe.apellido=info["apellido"]
            profe.email=info["email"]
            profe.profesion=info["profesion"]
            profe.save()
            return render (request, "Appcoder/inicio.html")
    else:
        form=ProfeForm(initial={"nombre":profe.nombre, "apellido" : profe.apellido, "email": profe.email, "profesion": profe.profesion})
    return render (request, "Appcoder/editarProfesor.html", {"formulario": form, "nombre_profesor":nombre_profesor})



#Vistas Basadas en clases



class EstudianteList(ListView, LoginRequiredMixin):
    model = Estudiante
    template_name="Appcoder/estudiantes_list.html"

class EstudianteDetalle(DetailView, LoginRequiredMixin):
    model = Estudiante
    template_name="Appcoder/estudiante_detalle.html"

class EstudianteCreacion(CreateView, LoginRequiredMixin):
    model = Estudiante
    success_url = reverse_lazy('estudiante_listar')
    fields = ['nombre', 'apellido', 'email']


class EstudianteUpdate(UpdateView, LoginRequiredMixin):
    model = Estudiante
    success_url= reverse_lazy('estudiante_listar')
    fields = ['nombre', 'apellido', 'email']

class EstudianteDelete(DeleteView, LoginRequiredMixin):
    model = Estudiante
    success_url = reverse_lazy('estudiante_listar')

#------------ LOGIN

def login_request(request):
    
    if request.method == 'POST':

        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid:
            usu= request.POST['username']
            clave= request.POST['password']

            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render (request, "Appcoder/inicio.html", {'form':form, 'mensaje': f"Bienvenido {usuario}"})
            else:
                return render (request, "Appcoder/login.html", {'form':form, 'mensaje': f"Usuario o clave incorrectos"})
        else:
            return render (request, "Appcoder/login.html", {'form':form, 'mensaje': f"Formulario invalido"})
    else:
        form = AuthenticationForm()
        return render (request, "Appcoder/login.html", {'form':form})


def register(request):

    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data["username"]
            form.save()
            return render (request, "Appcoder/inicio.html", {'form':form, 'mensaje': f"Usuario creado {username}"})
    else:
        form = UserRegisterForm()
    return render (request, "Appcoder/register.html", {'form':form})

