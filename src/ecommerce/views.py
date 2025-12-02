from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ContactForm
def home_page(request):
    context = {
        "title": "Página principal",
        "content": "Bem-vindo a página principal"
    }
    return render(request, "home_page.html", context)

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