from django.shortcuts import render
from django.http import HttpResponse
from .models import usuario
from .models import registro
from .models import proyectos

from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.



def index(request):
    global DNI_usuario
    usuarios_totales = usuario.objects.all() 
    usuario_1 = request.POST.get("usuario") # Obtengo el usuario de la vista
    contrasena = request.POST.get("contrasena") #Obtengo contraseña de la vista
    print("El nombre de usuario es: " + str(usuario_1))
    print("La contraseña del usuario es: " + str(contrasena))
    for each_usuario in usuarios_totales: # Comprueba para cada usuario
        if ((each_usuario.codigo_usuario == usuario_1) and (each_usuario.clave == contrasena)): # Compruebo credenciales
            print("Ingreso valido")
            print("El nombre de usuario es: " + str(usuario_1))
            print("La contraseña del usuario es: " + str(contrasena)) # Se immprime el usuario y contraseña
            DNI_usuario = each_usuario.DNI
            return HttpResponseRedirect(reverse("app_portafolio:portafolio_usuario")) #Voy a la vista dashboard
            
    return render(request,"app_portafolio/ingreso.html") # Caso contrario retorna la vista de login 

def create_new_user (request):

    if request.method == "POST":
        nombres= request.POST.get('nombres')
        apellidos= request.POST.get('apellidos')
        dni= request.POST.get('dni') 
        usuarios= request.POST.get('usuarios') 
        contraseña= request.POST.get('contraseña')  
        fotoperfil= request.POST.get('fotoperfil') 
        urlgithub= request.POST.get('urlgithub')
        foto_proy1= request.POST.get('foto_proy1')
        titulo_proy1= request.POST.get('titulo_proy1')
        descrip_proy1= request.POST.get('descrip_proy1') 
        foto_proy2= request.POST.get('foto_proy2') 
        titulo_proy2= request.POST.get('titulo_proy2') 
        descrip_proy2= request.POST.get('descrip_proy2') 
        foto_proy3= request.POST.get('foto_proy3') 
        titulo_proy3= request.POST.get('titulo_proy3') 
        descrip_proy3= request.POST.get('descrip_proy3') 


        usuario(DNI = str(dni), codigo_usuario = str(usuarios), clave=str(contraseña)).save()
        registro(nombres=str(nombres), apellidos=str(apellidos),dni=str(dni),usuarios=str(usuarios),contraseña=str(contraseña), fotoperfil=str(fotoperfil), urlgithub = str(urlgithub)).save()
        proyectos(dni_1=str(dni), foto_proy=str(foto_proy1),titulo_proy=str(titulo_proy1),descrip_proy=str(descrip_proy1)).save()
        proyectos(dni_1=str(dni), foto_proy=str(foto_proy2),titulo_proy=str(titulo_proy2),descrip_proy=str(descrip_proy2)).save()
        proyectos(dni_1=str(dni), foto_proy=str(foto_proy3),titulo_proy=str(titulo_proy3),descrip_proy=str(descrip_proy3)).save()
        #print(str(nombres))
        #print(str(apellidos))
        #print(str(dni))
        #print(str(usuarios))
        #print(str(contraseña))
        #print(str(fotoperfil))
        #print(str(urlgithub))
        #print(str(foto_proy1))
        #print(str(titulo_proy1))
        #print(str(descrip_proy1))
        #print(str(foto_proy2))
        #print(str(titulo_proy2))
        #print(str(descrip_proy2))
        #print(str(foto_proy3))
        #print(str(titulo_proy3))
        #print(str(descrip_proy3))

    return render(request, "app_portafolio/create_new_user.html")

def portafolio_usuario (request):
    lista_proyectos1 =[]
    lista_proyectos2 =[]
    usuario_usar = registro.objects.get(dni=DNI_usuario)

    proyectos_totales= proyectos.objects.filter(dni_1=DNI_usuario)
    for proyecto_1 in proyectos_totales[0:3]:
        lista_proyectos1.append(proyecto_1)

    if (len(proyectos_totales) != 3):
        for proyecto_2 in proyectos_totales[3:len(proyectos_totales)]:
            lista_proyectos2.append(proyecto_2)
    print(lista_proyectos2)
    return render(request, "app_portafolio/index.html",{
        'usuario_usar': usuario_usar,
        'lista_proyectos1': lista_proyectos1,
        'lista_proyectos2': lista_proyectos2
    })


    