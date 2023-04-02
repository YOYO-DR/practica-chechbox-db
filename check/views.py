from django.shortcuts import render
from django.http import JsonResponse
from .models import MiModelo
from time import sleep

def actualizar_valor(request, id):
    try:
      objeto = MiModelo.objects.get(id=id)
      nuevo_valor = not objeto.valor
      objeto.valor = nuevo_valor
      objeto.save()
      return JsonResponse({'status': 'ok'})
    except Exception as e:
       print(e)
       return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def vista(request):
  context = {
     'objetos':MiModelo.objects.all()
  }
  if not context['objetos']:
     MiModelo(valor=False,nombre='checkbox').save()
  return render(request, 'index.html',context)

