from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render,redirect
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import LoginForm, RegisterForm
from django.conf import settings

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
                    "form": form
              }
    print("User logged in")
    print(request.user.is_authenticated)
    next_ = request.GET.get('next')
    next_post = request.POST.get('next') #redirect_path = next_ or next_post or None
    redirect_path = next_ or next_post or None    
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
            if url_has_allowed_host_and_scheme( redirect_path, request.get_host() ):
                return redirect( redirect_path )
            else:
                # Redireciona para uma página de sucesso.
                return redirect("/")
        else:
            #Retorna uma mensagem de erro de 'invalid login'.
            print("Login inválido")
    return render(request, "accounts/login.html", context)

# def logout_page(request):
#     context = {
#                 "content": "Você efetuou o logout com sucesso! :)"
#               }
#     logout(request)
#     return render(request, "accounts/logout.html", context)

# estou usando o LogoutView do django
# def logout_process(request):
#     # Apenas processa o logout se for um envio POST
#     if request.method == "POST":
#         if request.user.is_authenticated:
#             # EXECUTA o logout
#             logout(request)
#             # Adiciona uma mensagem de sucesso para ser exibida após o redirecionamento
#             messages.success(request, "Você saiu da sua conta com sucesso.")
        
#         # Redireciona o usuário para a página inicial
#         return redirect(settings.LOGOUT_REDIRECT_URL)
    
#     # Se alguém tentar acessar essa URL via GET (diretamente), redirecionamos
#     return redirect("/")


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
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "accounts/register_v2.html", context) 