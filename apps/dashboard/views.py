from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    """Carrega dashboard com dados da empresa"""
    if request.method == 'GET':
        return render(request, 'dashboard/index.html')
    else:
        return HttpResponse(status=405)
