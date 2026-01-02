from django.contrib import admin
from .models import Product
from django.db.models.functions import Lower

class ProductAdmin(admin.ModelAdmin):

    # 1. Colunas que aparecem na tabela
    list_display = ('title_display', 'slug', 'price', 'active')

    @admin.display(ordering=Lower('title'), description='Title')
    def title_display(self, obj):
        return obj.title

    # 2. Torna o preço e o status 'ativo' editáveis sem precisar clicar no produto
    list_editable = ('price', 'active')

    # 3. Cria uma barra de busca (procura no título e no slug)
    search_fields = ('title', 'slug')

    # 4. Cria filtros na lateral direita (bom para filtrar produtos ativos/inativos)
    list_filter = ('active', ('price', admin.AllValuesFieldListFilter))

    # 5. Define a ordem padrão (do mais recente para o mais antigo)
    ordering = ('price',)

    def get_ordering(self, request):
        return [Lower('title')]  # Ordena pelo título em minúsculo (case-insensitive)

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)