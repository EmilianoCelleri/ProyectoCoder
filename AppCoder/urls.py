from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('curso/', curso),
    path('cursos/', cursos, name="Cursos"),
    path('profesores/', profesores, name="Profesores"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('entregables/', entregables, name="Entregables"),
    path('', inicio, name="Inicio"),
    path('cursoFormulario/', cursoFormulario, name="cursoFormulario"),
    path('profeFormulario/', profeFormulario, name="profeFormulario"),
    path('busquedaComision/', busquedaComision, name="busquedaComision"),
    path('buscar/', buscar, name="buscar"),
    path('leerProfesores/', leerProfesores, name="leerProfesores"),
    path('eliminarProfesor/<nombre_profesor>', eliminarProfesor, name="eliminarProfesor"),
    path('editarProfesor/<nombre_profesor>', editarProfesor, name="editarProfesor"),



    #Vista clases

    path('estudiante/list/', EstudianteList.as_view(), name='estudiante_listar'),
    path('estudiante/<pk>', EstudianteDetalle.as_view(), name='estudiante_detalle'),
    path('estudiante/nuevo/', EstudianteCreacion.as_view(), name='estudiante_crear'),
    path('estudiante/editar/<pk>', EstudianteUpdate.as_view(), name='estudiante_editar'),
    path('estudiante/borrar/<pk>', EstudianteDelete.as_view(), name='estudiante_borrar'),

    #LOGIN

    path('login/', login_request, name="login"),
    path('register/', register, name="register"),
    path('logout/', LogoutView.as_view (template_name='AppCoder/logout.html'), name='logout'),

] 