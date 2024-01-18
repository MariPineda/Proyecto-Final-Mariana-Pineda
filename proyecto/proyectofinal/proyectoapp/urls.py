
from django.urls import path

from django.contrib.auth.views import LogoutView

from proyectoapp.views import (
    socios, 
    libros, 
    socios_formulario,
    libros_formulario,
    busqueda_socios,
    buscar_socios,
    listar_libros,
    eliminar_libros,
    editar_libros,
    login_request,
    registrar,
    editar_perfil,
    avatar,
    SociosList,
    SociosDetalle,
    SociosCreacion,
    SociosUpdate,
    SociosDelete,
    about_me,
    admin,
    index,
)

urlpatterns = [
    path("socios/", socios, name='socios'),
    path("libros/", libros, name='libros'),
    path("sociosFormulario/", socios_formulario, name='socios_formulario'),
    path("librosFormulario/", libros_formulario, name='libros_formulario'),
    path("busquedaSocios/", busqueda_socios, name='busqueda_socios'),
    path("buscar/", buscar_socios, name='buscar_socios'),
    path("listarLibros/", listar_libros, name='listar_libros'),
    path("eliminarLibros/<nombre_libro>/", eliminar_libros, name='eliminar_libros'),
    path('editar_libros/<nombre_libro>', editar_libros, name='editar_libros'),
    path('socios/list', SociosList.as_view(), name = 'List'),
    path('detalle-socios/<pk>', SociosDetalle.as_view(), name='Detail'),
    path('editar-socios/<pk>', SociosUpdate.as_view(), name='Edit'),
    path('crear-socios', SociosCreacion.as_view(), name='New'),
    path('borrar-socios/<pk>', SociosDelete.as_view(), name='Delete'),
    path('login', login_request, name='Login'),
    path('registrar', registrar, name='Registrar'),
    path('editar_perfil', editar_perfil, name='editar_perfil'),
    path('logout', LogoutView.as_view(template_name="logout.html"), name='Logout'),
    path('avatar', avatar, name='avatar'),
    path("about/", about_me, name='about_me'),
    path("admin/", admin, name='admin'),
    path('', index, name='index'),
]