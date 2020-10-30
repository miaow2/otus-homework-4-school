from django.shortcuts import render
from django.views.generic import View


def frontend_view(request):
  return render(request, 'index.html')
