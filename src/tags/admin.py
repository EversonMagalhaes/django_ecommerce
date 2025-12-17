from django.contrib import admin

# Register your models here.
from .models import Tag

from .forms import TagAdminModelForm # Importe o formulário

class TagAdmin(admin.ModelAdmin):
    # Use o formulário personalizado
    form = TagAdminModelForm 
    
    # ... (outras configurações do Admin)



admin.site.register(Tag,TagAdmin)