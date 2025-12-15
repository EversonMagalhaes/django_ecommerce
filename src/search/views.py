from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from products.models import Product

class SearchProductView(ListView):
    template_name = "products/list.html"
    def get_queryset(self, *args, **kargs):
        request = self.request
        # return Product.objects.filter(title__icontains = 'Camiseta')
        print('Solicitação', request)
        result = request.GET
        print('Resultado: ', result)
        query = result.get('q', None) # result['q']
        print('Consulta', query)
        if query is not None:
            return Product.objects.filter(title__icontains = query)
        return Product.objects.featured()
    
