from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import RegisterForm,LoginForm

def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login()
            if user:
                login(request, user)
                messages.success(request, f'Bienvenido, {user.username}!')
                return redirect('home')  # Asegúrate de tener una URL nombrada 'home'
            else:
                messages.error(request, 'Credenciales inválidas.')
    else:
        form = LoginForm()
    
    return render(request, 'login_register.html', {'form': form})

# Si aún quieres mantener una vista separada para el registro, puedes hacerlo así:
def registro_usuario(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.register()
            login(request, user)
            messages.success(request, f'Cuenta creada para {user.username}!')
            return redirect('home')  # Asegúrate de tener una URL nombrada 'home'
    else:
        form = RegisterForm(initial={'action': 'register'})
    
    return render(request, 'registro_usuario.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión exitosamente.")
    return redirect('home')  # Asume que tienes una URL nombrada 'home'
