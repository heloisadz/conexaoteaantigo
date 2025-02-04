from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout
from django.shortcuts import redirect

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user =  User.objects.filter(username=username).first()

        if user:
            return HttpResponse ('Usuário com esse username já existe')
        #o que vem dps da igualdade é referente a este codigo
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name )
        user.save()
        
    return render(request, 'home.html')
    return HttpResponse(username)

def login(request):
    if request.method =='GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

    if user:
        login_django(request, user)
        #return HttpResponse ('Usuario autenticadoo')
        return HttpResponseRedirect('/auth/home/')
    
        
    
    else:
        return HttpResponse('Email ou senha inválidos :(')
    

    return render(request, 'login.html')


    
def home(request):
    return render(request, 'home.html')

    


def logout(request):
    
    messages.success(request, 'Você foi desconectado com sucesso.')
    return redirect('login')  # Certifique-se de que 'login' não está apontando para a mesma URL de logout