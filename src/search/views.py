from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from products.models import Product
# from django.db.models import Q
from unidecode import unidecode

class SearchProductView(ListView):
    template_name = "search/view.html"



    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context
    

    def get_queryset(self, *args, **kargs):
        query = self.request.GET.get('q')

        if query:
            # 1. Limpa o termo do usuário (query_limpo)
            query_limpo = unidecode(query.strip()).lower() # Garante minúsculas
            
            # 2. Consulta o campo auxiliar (search_title)
            return Product.objects.filter(
                search_title__icontains=query_limpo
            ).distinct()
        
        return Product.objects.featured()

    # def get_queryset(self, *args, **kargs):
    #     request = self.request
    #     query = request.GET.get('q') # Recupera o termo de busca

    #     if query: # Testa se a query não é None e não é string vazia

    #         # 1. Normaliza a query para remover acentos e caracteres especiais:
    #         query_limpo = unidecode(query.strip())
    #         print(f"Consulta Original: {query}, Consulta Limpa: {query_limpo}")
            
    #         # 2. Constrói a consulta OR usando Q objects
    #         final_query = (
    #             # Busca pelo termo original (cobre acentos corretos):
    #             Q(title__icontains=query) 
    #             |
    #             # Busca pelo termo limpo/sem acento (cobre erros de digitação de acento):
    #             Q(title__icontains=query_limpo) 
    #         )

    #         # 3. Retorna os resultados filtrados
    #         return Product.objects.filter(final_query)

    # def get_queryset(self, *args, **kargs):
    #     request = self.request
    #     # return Product.objects.filter(title__icontains = 'Camiseta')
    #     # print('Solicitação', request)
    #     result = request.GET
    #     # print('Resultado: ', result)
    #     query = result.get('q', None) # result['q']
    #     print('Consulta', query)
    #     if query is not None:
    #         return Product.objects.filter(title__icontains = query)
    #     return Product.objects.featured()
    
