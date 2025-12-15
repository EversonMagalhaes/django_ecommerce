from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib import messages

def home_page(request):
    context = {
        "title": "Página principal",
        "content": "Bem-vindo a página principal"
    }
    if request.user.is_authenticated:
        context["premium_content"] = "Você é um usuário Premium"
    return render(request, "home_page.html", context)
    #return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "Página sobre",
        "content": "Bem-vindo a página sobre"
    }
    return render(request, "about/view.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Página de contato",
        "content": "Bem-vindo a página de contato",
        'form': contact_form
    }
    if request.method == 'POST':
        print(request.POST)

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        # 1. SALVAR OS DADOS AQUI (ou enviar email, etc.)
            
        # 2. ADICIONAR A MENSAGEM DE SUCESSO
        messages.success(request, 'Sua mensagem foi enviada com sucesso!')
            
        # 3. FAZER O REDIRECIONAMENTO (LIMPA O FORMULÁRIO!)
        # Substitua 'nome_da_url_de_contato' pelo nome que você deu a essa view no seu urls.py
        return redirect('contact')

    return render(request, "contact/view.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
                    "form": form
              }
    print("User logged in")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password) 
        print(user)
        print(request.user.is_authenticated)
        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            print("Login válido")
            print(request.user.is_authenticated)
            # Redireciona para uma página de sucesso.
            return redirect("/")
        else:
            #Retorna uma mensagem de erro de 'invalid login'.
            print("Login inválido")
    return render(request, "auth/login.html", context)

# def logout_page(request):
#     context = {
#         "content": "Você efetuou o logout com sucesso."
#     }
#     logout(request)
#     return render(request, "auth/logout.html", context)

def logout_process(request):
    # Apenas processa o logout se for um envio POST
    if request.method == "POST":
        if request.user.is_authenticated:
            # EXECUTA o logout
            logout(request)
            # Adiciona uma mensagem de sucesso para ser exibida após o redirecionamento
            messages.success(request, "Você saiu da sua conta com sucesso.")
        
        # Redireciona o usuário para a página inicial
        return redirect("/") 
    
    # Se alguém tentar acessar essa URL via GET (diretamente), redirecionamos
    return redirect("/")


# User = get_user_model()
# def register_page(request):
#     form = RegisterForm(request.POST or None)
#     context = {
#                     "form": form
#               }
#     if form.is_valid():
#         print(form.cleaned_data)
#         username = form.cleaned_data.get("username")
#         email = form.cleaned_data.get("email")
#         password = form.cleaned_data.get("password")
#         new_user = User.objects.create_user(username, email, password)
#         print(new_user)
#     return render(request, "auth/register_v2.html", context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
                    "form": form
              }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        
        # 1. CRIAÇÃO DO NOVO USUÁRIO
        new_user = User.objects.create_user(username, email, password)
        print(f"Novo usuário criado: {new_user}")
        
        # 2. AUTENTICAÇÃO E LOGIN AUTOMÁTICO
        # Autentica o usuário recém-criado para obter o objeto completo.
        # Isso garante que todas as verificações de backend sejam feitas.
        user_to_login = authenticate(request, username=username, password=password)
        
        if user_to_login is not None:
            # Seta o usuário na sessão (Faz o login)
            login(request, user_to_login)
            print("Login automático realizado com sucesso!")
            
            # 3. REDIRECIONAMENTO
            # Redireciona para a página inicial (ou 'home', se tiver esse nome de URL)
            return redirect("/") # Você pode usar reverse('home') se estiver definido
            
    return render(request, "auth/register_v2.html", context)