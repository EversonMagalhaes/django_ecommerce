from django.db.models.signals import pre_save
from django.dispatch import receiver

# Importe apenas o modelo que dispara o signal
from .models import Tag 

# Importe a função geradora do outro app (Products)
from products.utils import unique_slug_generator

@receiver(pre_save, sender=Tag)
def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.title = instance.clean_title()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

