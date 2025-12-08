#from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
#from django.shortcuts import render, get_object_or_404

from .models import Product

# class ProductFeaturedListView(ListView):
#     template_name = "products/list.html"
    
#     def get_queryset(self, *args, **kwargs):
#         return Product.objects.featured()

# class ProductFeaturedDetailView(DetailView):
#     queryset = Product.objects.all().featured()
#     template_name = "products/featured-detail.html"

#Class Based View
class ProductListView(ListView):
    #traz todos os produtos do banco de dados sem filtrar nada 
    queryset = Product.objects.all()
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context


class ProductDetailSlugView(DetailView):
    # O Manager customizado (Product.objects.all()) já filtra por active=True
    queryset = Product.objects.all() 
    template_name = "products/detail2.html"

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        
        # 1. Busca o produto, mas apenas entre os ATIVOS
        # Se o produto não for encontrado (ou for inativo), ele levanta 404
        instance = get_object_or_404(Product.objects.all(), slug=slug)
        
        # O bloco try/except complexo é simplificado pelo get_object_or_404,
        # pois o queryset já garante que ele só buscará ativos.
        
        return instance



# class ProductDetailSlugView(DetailView):
#     queryset = Product.objects.all()
#     template_name = "products/detail.html"

#     def get_object(self, *args, **kwargs):
#         slug = self.kwargs.get('slug')
#         #instance = get_object_or_404(Product, slug = slug, active = True)
#         try:
#             instance = Product.objects.get(slug = slug)
#         except Product.DoesNotExist:
#             raise Http404("Não encontrado!")
#         except Product.MultipleObjectsReturned:
#             qs = Product.objects.filter(slug = slug, active = True)
#             instance =  qs.first()
#         return instance


# #Function Based View
# def product_list_view(request):
#     queryset = Product.objects.all()
#     context = {
#         'qs': queryset,
#         'object_list': queryset
#     }
#     return render(request, "products/list.html", context)

# #Class Based View
# class ProductDetailView(DetailView):
#     #traz todos os produtos do banco de dados sem filtrar nada 
#     #queryset = Product.objects.all() 
#     template_name = "products/detail.html"
    
#     # def get_context_data(self, *args, **kwargs):
#     #     context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
#     #     print(context)
#     #     return context
#     def get_object(self, *args, **kwargs):
#         pk = self.kwargs.get('pk')
#         instance = Product.objects.get_by_id(pk)
#         if instance is None:
#             raise Http404("Esse produto não existe!")
#         return instance

# #Function Based View
# def product_detail_view(request, pk = None, *args, **kwargs):
#     #instance = get_object_or_404(Product, pk = pk) #← maneira mais simples de testar
#     # maneira 1 de testar
#     # try:
#     #     instance = Product.objects.get(id = pk)
#     # except Product.DoesNotExist:
#     #     print("Nenhum produto encontrado aqui!")
#     #     raise Http404("Esse produto não existe!")
    
#     #qs = Product.objects.filter(id = pk) # ← maneira 2 e 3 de testar
#     #if qs.exists(): ← maneira 2 de testar
#     # if qs.count() == 1: #← maneira 3 de testar
#     #     instance = qs.first()
#     # else:
#     #     raise Http404("Esse produto não existe!")
#     instance = Product.objects.get_by_id(pk)
#     print(instance)
#     if instance is None:
#         raise Http404("Esse produto não existe!")
    
#     context = {
#         'object': instance
#     }
#     return render(request, "products/detail.html", context)