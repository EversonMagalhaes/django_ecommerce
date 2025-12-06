from django.db.models.signals import pre_save
from django.dispatch import receiver


# Importe o seu modelo (Product) e a função geradora
from .models import Product
from .utils import unique_slug_generator

# O decorator @receiver é a forma moderna e mais limpa de fazer o connect
@receiver(pre_save, sender=Product)
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    """
    Gera um slug único e seguro antes que o objeto seja salvo.
    """
    if not instance.slug:
        # Chama a sua função para garantir que o slug é gerado a partir do título
        instance.slug = unique_slug_generator(instance)

# Nota: Não precisamos do pre_save.connect() aqui, pois o @receiver já faz isso.