# app_Delrio/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Venta, Cliente, Producto # Importa los modelos

# ==========================================
# VISTAS PARA VENTA
# ==========================================

def inicio_Delrio(request):
    """
    Vista principal del sistema.
    """
    return render(request, 'inicio.html')

def ver_ventas(request):
    """
    Muestra una lista de todas las ventas.
    """
    ventas = Venta.objects.all().order_by('-fech_venta')
    return render(request, 'Ventas/ver_venta.html', {'ventas': ventas})


def agregar_venta(request):
    """
    Permite agregar una nueva venta.
    """
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()

    if request.method == 'POST':
        try:
            id_clie = request.POST.get('id_clie')
            id_prod = request.POST.get('id_prod')
            total_venta = request.POST.get('total_venta')
            estado = request.POST.get('estado')
            id_empl = request.POST.get('id_empl')

            cliente_obj = get_object_or_404(Cliente, id=id_clie)
            producto_obj = get_object_or_404(Producto, id=id_prod)

            Venta.objects.create(
                id_clie=cliente_obj,
                id_prod=producto_obj,
                total_venta=total_venta,
                estado=estado,
                id_empl=id_empl,
            )
            return redirect('ver_ventas')
        except Exception as e:
            # Aquí puedes manejar errores si los datos no son válidos
            print(f"Error al agregar venta: {e}")
            # Puedes añadir un mensaje de error al contexto para mostrar en la plantilla
            return render(request, 'Ventas/agregar_venta.html', {
                'clientes': clientes,
                'productos': productos,
                'error_message': f"Hubo un error al guardar la venta: {e}"
            })

    return render(request, 'Ventas/agregar_venta.html', {'clientes': clientes, 'productos': productos})


def actualizar_venta(request, pk):
    """
    Muestra el formulario para actualizar una venta existente.
    """
    venta = get_object_or_404(Venta, pk=pk)
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    return render(request, 'Ventas/actualizar_venta.html', {
        'venta': venta,
        'clientes': clientes,
        'productos': productos
    })


def realizar_actualizacion_venta(request, pk):
    """
    Procesa la actualización de una venta.
    """
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        try:
            id_clie = request.POST.get('id_clie')
            id_prod = request.POST.get('id_prod')
            total_venta = request.POST.get('total_venta')
            estado = request.POST.get('estado')
            id_empl = request.POST.get('id_empl')

            venta.id_clie = get_object_or_404(Cliente, id=id_clie)
            venta.id_prod = get_object_or_404(Producto, id=id_prod)
            venta.total_venta = total_venta
            venta.estado = estado
            venta.id_empl = id_empl
            venta.save()
            return redirect('ver_ventas')
        except Exception as e:
            print(f"Error al actualizar venta: {e}")
            clientes = Cliente.objects.all()
            productos = Producto.objects.all()
            return render(request, 'Ventas/actualizar_venta.html', {
                'venta': venta,
                'clientes': clientes,
                'productos': productos,
                'error_message': f"Hubo un error al actualizar la venta: {e}"
            })
    return redirect('ver_ventas') # Redirige si se accede por GET


def borrar_venta(request, pk):
    """
    Borra una venta.
    """
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('ver_ventas')
    # Opcional: puedes renderizar una página de confirmación de borrado
    return render(request, 'Ventas/borrar_venta.html', {'venta': venta})