from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render


def listado_modulos(request):
    modulos = [
        {
            'nombre': 'ARTICULOS',
            'url': 'can_view_cliente',
            'app': 'articulos',
            'icono': 'fa-bolt',  # Icono para el módulo 'Ventas'
            'submodulos': [
                {
                    'app': 'articulos',
                    'nombre': 'MÓDULOS',
                    'permiso': 'can_view_modulo',
                    'url': 'articulo_modulo_index',#clientes_index
                    'icono': 'fa-search',  # Icono para el submódulo 'Ver Ventas'
                },
                {
                    'app': 'articulos',
                    'nombre': 'INVERSORES',
                    'permiso': 'can_view_inversor',
                    'url': 'articulo_inversor_index',#clientes_index
                    'icono': 'fa-search',  # Icono para el submódulo 'Ver Ventas'
                },
                {
                    'app': 'articulos',
                    'nombre': 'MONITOREOS',
                    'permiso': 'can_view_monitoreo',
                    'url': 'articulo_monitoreo_index',#clientes_index
                    'icono': 'fa-search',  # Icono para el submódulo 'Ver Ventas'
                },
                {
                    'app': 'articulos',
                    'nombre': 'ESTRUCTURAS',
                    'permiso': 'can_view_estructura',
                    'url': 'articulo_estructura_index',#clientes_index
                    'icono': 'fa-search',  # Icono para el submódulo 'Ver Ventas'
                },
               
            ]
        },
        {
            'nombre': 'CLIENTES',
            'url': 'can_view_cliente',
            'app': 'clientes',
            'icono': 'fa-users',  # Icono para el módulo 'Ventas'
            'submodulos': [
                {
                    'app': 'clientes',
                    'nombre': 'clientes',
                    'permiso': 'can_view_cliente',
                    'url': 'clientes_index',#clientes_index
                    'icono': 'fa-search',  # Icono para el submódulo 'Ver Ventas'
                },
                {
                    'app': 'crm',
                    'nombre': 'empresas',
                    'permiso': 'can_view_empresa',
                    'url': 'empresa_index',#clientes_index
                    'icono': 'fa-search',  # Icono para el submódulo 'Ver Ventas'
                }
               
            ]
        },
        #=====================================
        #          CUESTIONARIOS
        #=====================================
        {
            'nombre': 'CUESTIONARIOS',
            'url': 'cuestionarios_index',
            'app': 'cuestionarios',
            'icono': 'fa-book',  # Icono para el módulo 'Ventas'
            'submodulos': [
                {
                    'app': 'cuestionarios',
                    'nombre': 'CUESTIONARIOS',
                    'permiso': 'can_view_cuestionarios',
                    'url': 'cuestionarios_index',#clientes_index
                    'icono': 'fa-search',  # Icono para el submódulo 'Ver Ventas'
                },
                
               
            ]
        },
        #=====================================
        #   CONFIGURACIONES DEL SISTEMA
        #=====================================
        {
            'nombre': 'CONFIGURACION',
            'url': 'user_index',
            'app': 'usuario',
            'icono': 'fa-cogs',  # Icono para el módulo 'USUARIOS'
            'submodulos': [
                #=====================================
                #  SUBMÓDULO DE USUARIOS
                #=====================================
                {
                    'app': 'usuario',
                    'nombre': 'Usuarios',
                    'permiso': 'can_view_user',
                    'url': 'user_index',
                    'icono': 'fa-eye',  # Icono para el submódulo 'Ver Usuarios'
                },
                ##=====================================
                ##  SUBMÓDULO DE GRUPOS
                ##=====================================
                {
                    'app': 'auth',
                    'nombre': 'Grupos',
                    'permiso': 'can_view_grupo',
                    'url': 'grupos_index',
                    'icono': 'fa-eye',  # Icono para el submódulo 'Ver Usuarios'
                },
                ##=====================================
                ##  SUBMÓDULO DE CONSTANTES DE INGENIERIA
                ##=====================================
                #{
                #    'app': 'ingenieria',
                #    'nombre': 'COSNTANTES',
                #    'permiso': 'can_view_constantes',
                #    'url': 'ingenieria_constante_index',
                #    'icono': 'fa-eye',  # Icono para el submódulo 'Ver Usuarios'
                #},
                #{
                #    'app': 'ingenieria',
                #    'nombre': 'RADIACIONES',
                #    'permiso': 'can_view_radiacion',
                #    'url': 'ingenieria_radiacion_index',
                #    'icono': 'fa-eye',  # Icono para el submódulo 'Ver Usuarios'
                #}
                
            ]
        },
    ]
    
    if request.user.is_authenticated:
        #print( request.user.get_all_permissions(),'permisos')
        permisos_usuario = request.user.get_all_permissions()
        #print(permisos_usuario,'permisos')
        modulos_accesibles = []

        for modulo in modulos:
            modulos_acc = {
                'nombre': modulo['nombre'],
                'url': "",#modulo['url'],
                'icono': modulo['icono'],  # Incluir el ícono del módulo
                'submodulos': [],
            }
            for submodulo in modulo['submodulos']:
                if f'{submodulo["app"]}.{submodulo["permiso"]}' in permisos_usuario:
                    modulos_acc['submodulos'].append(submodulo)
            
            if modulos_acc['submodulos']:
                modulos_accesibles.append(modulos_acc)
                
        
        #print(modulos_accesibles, 'hay usuarios')
        #print(permisos_usuario,'hay usuarios')
        return {'modulos_accesibles': modulos_accesibles}
        #print(modulos_accesibles,'no hay usuarisdsd')    
    return {'modulos_accesibles': []}
