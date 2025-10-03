from django.shortcuts import render

# Create your views here.
def index(request):
    clientes = [
        {
            'nombre': 'Ana López',
            'email': 'ana.lopez@ejemplo.com',
            'telefono': '555-1234'
        },
        {
            'nombre': 'Carlos Ruiz',
            'email': 'carlos.ruiz@ejemplo.com',
            'telefono': '555-5678'
        },
        {
            'nombre': 'Marta García',
            'email': 'marta.garcia@ejemplo.com',
            'telefono': '555-9012'
        },
    ]
    context = {
        'clientes': clientes
    }
    return render(request, 'index.html', context)
