from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
     #=======================================================
    #                   CLIENTES   
    #=======================================================
    path('clientes/',                 login_required(views.index_cliente), name='clientes_index'),
    path('clientes/create/',          login_required(views.create_cliente), name='clientes_create'),
    path('clientes/view/<int:id>/',   login_required(views.view_cliente), name='cliente_view'),
    path('clientes/update/<int:id>/', login_required(views.update_cliente), name='cliente_update'),
    path('clientes/delete/<int:id>/', login_required(views.delete_cliente), name='cliente_delete'),
    path('clientes/cliente-list-ajax/', login_required(views.index_list_ajax_cliente), name='list_ajax_clientes'),    
    #path('groups/',                login_required(views.index), name='grupos_index'),
    #path('groups/create/',         login_required(views.create), name='grupos_create'),
    #path('groups/view/<int:id>/',  login_required(views.view), name='grupos_view'),
    #path('groups/update/<int:id>/',login_required(views.update), name='grupos_update'),
    #path('delete/<int:id>/',       login_required(views.delete), name='grupos_delete'),
    #
    #
    #
    #
    #
    #
    ##AJAX
    #path('grupos-list-ajax/', login_required(views.index_list_ajax), name='list_ajax_grupos'),
    
]