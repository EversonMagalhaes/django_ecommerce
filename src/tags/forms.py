from django import forms
from .models import Tag
from unidecode import unidecode # Vamos precisar da função de normalização

class TagAdminModelForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

    # Sobrescrevemos o método clean() do formulário
    def clean_title(self):
        title = self.cleaned_data.get('title')
        
        # 1. Normaliza o dado que veio do formulário (Ex: "Tênis Casual" -> "tenis casual")
        normalized_title = unidecode(title.strip()).lower()
        
        # 2. Re-associa o dado LIMPO de volta ao formulário
        self.cleaned_data['title'] = normalized_title
        
        # 3. Retorna o dado original para o pipeline de validação
        # (O Django fará a validação de unicidade na linha abaixo!)
        return title # IMPORTANTE: Retorna o original, mas o self.cleaned_data já está modificado

    # OBS: O Django agora vai usar o valor normalizado para checar o unique=True.
    # Se o valor normalizado já existe no banco, o Django disparará ValidationError
    # no formulário, e não o IntegrityError do banco!