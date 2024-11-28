from django.shortcuts import render
from users.models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
# Create your views here.





# SQL INYECTION

def get_user_by_email(request):
    email = request.GET.get('email')
    user = CustomUser.objects.filter(email=email).first()  # query seguro con ORM
    return render(request, 'user_profile.html', {'user': user})


# CONTROL DE SECUESTRO DE SESIÓN

def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            request.session.cycle_key()  # Regenera el ID de sesión después del login
            return redirect('home')  # Redirige a la página de inicio después de login exitoso
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# ENCRIPTAR CONTRASEÑAS

def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # Crear el usuario con contraseña encriptada automáticamente
        user = User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')  # Redirige a la página de inicio de sesión después del registro
    return render(request, 'register.html')



#VISTA HOME

def home(request):
    return render(request, 'home.html')  # Renderiza la plantilla home.html




# VISTA REGISTRO DE USER


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario
            return redirect('login')  # Redirige a la página de inicio de sesión
    else:
        form = CustomUserCreationForm()  # Muestra un formulario vacío

    return render(request, 'register.html', {'form': form})




# VISTA INICIO DE SESIÓN DE USER


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirige al inicio después del login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
