from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Cliente,DireccionClientes
from .forms import ClienteForm, DireccionForm
from django.contrib.auth.decorators import permission_required
from datetime import datetime

#==================================================================
#                      CLIENTES
#==================================================================
@permission_required('clientes.can_view_cliente', raise_exception=True)
def index_cliente(request):
    return render(request, 'clientes/index.html')

@permission_required('clientes.can_view_cliente', raise_exception=True)
def view_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    try:
        direccion = DireccionClientes.objects.get(cliente=cliente)
    except DireccionClientes.DoesNotExist:
        direccion = DireccionClientes(cliente=cliente)
    
    return render(request, 'clientes/view.html', {'cliente': cliente, 'direccion': direccion})

@permission_required('clientes.can_create_cliente', raise_exception=True)
def create_cliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        direccion_form = DireccionForm(request.POST)
        #print(request.POST)
        if cliente_form.is_valid() and direccion_form.is_valid():
            cliente = cliente_form.save(commit=False)
            cliente.created_by = request.user
            cliente.save()
            direccion = direccion_form.save(commit=False)
            if  direccion_form.cleaned_data.get('estado') and direccion_form.cleaned_data.get('municipio') and direccion_form.cleaned_data.get('colonia'):
                direccion.cliente = cliente
                direccion.save()
            #print(direccion_form.errors)
            return redirect('cliente_view', id=cliente.id)
    else:
        cliente_form = ClienteForm()
        direccion_form = DireccionForm()
        #estados = Estado.objects.all()
       
    
    return render(request, 'clientes/create.html', {
        'cliente_form': cliente_form,
        'direccion_form': direccion_form,
        #'estados': estados,
    })
    #return render(request, 'clientes/create.html')

@permission_required('clientes.can_update_cliente', raise_exception=True)
def update_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    try:
        direccion = DireccionClientes.objects.get(cliente=cliente)
    except DireccionClientes.DoesNotExist:
        direccion = DireccionClientes(cliente=cliente)
    
    if request.method == 'POST':
        #print(request.POST)
        cliente_form = ClienteForm(request.POST, instance=cliente)
        direccion_form = DireccionForm(request.POST, instance=direccion)
        
        if cliente_form.is_valid() and direccion_form.is_valid():
            
            cliente = cliente_form.save(commit=False)
            cliente.updated_by = request.user
            print(request.user.id)
            cliente.save()
            direccion = direccion_form.save(commit=False)
            if  direccion_form.cleaned_data.get('estado') and direccion_form.cleaned_data.get('municipio') and direccion_form.cleaned_data.get('colonia'):
                direccion.cliente = cliente
                direccion.save()
            #print(direccion_form.errors)
            
            return redirect('cliente_view', id=cliente.id)
    else:
        cliente_form = ClienteForm(instance=cliente )
        direccion_form = DireccionForm( instance=direccion)
        
       
    
    return render(request, 'clientes/update.html', {
        'model': cliente,
        'cliente_form': cliente_form,
        'direccion_form': direccion_form,
        
    })
   
def delete_cliente(request, id):
    pass
    #return render(request, 'clientes/delete.html')
@permission_required('clientes.can_view_cliente', raise_exception=True)
def index_list_ajax_cliente(request):
    draw = int(request.GET.get('draw', 1))
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    search_value = request.GET.get('search[value]', '')

    # Filtrado por búsqueda
    clients = Cliente.objects.all()
    if search_value:
       clients = clients.filter(
        Q(nombres__icontains=search_value) |
        #Q(apellido_paterno__icontains=search_value) |
        #Q(email__icontains=search_value)|
        Q(id__icontains=search_value)
        #Q(username__icontains=search_value)
    )
    # Paginación
    paginator = Paginator(clients, length)
    page_number = (start // length) + 1
    page_obj = paginator.get_page(page_number)

    # Serializar datos
    data = [
        {
            "id": s.id,
            "full_name": f"{s.nombres}  {s.apellido_paterno} {s.apellido_materno}",
            "phone": str(s.telefono),
            "phone2": str(s.telefono2),
            'tipo': s.get_tipo_display(),
            'estado': s.get_status_display(),
            
            "email": str(s.email),
            #"created_at": s.created_at,
            "created_at": datetime.fromtimestamp(s.created_at).strftime("%d-%h-%Y %H:%M:%S") if s.created_at else 'N/A'
            #"created_by": str(s.created_by.username) if s.created_by else "",
        }
        for s in page_obj
    ]

    return JsonResponse({
        "draw": draw,
        "recordsTotal": paginator.count,
        "recordsFiltered": paginator.count,
        "data": data
    })
