from ecommerce.utils import unique_order_id_generator
from django.db.models.signals import pre_save
from .models import Order
from django.dispatch import receiver

@receiver(pre_save, sender=Order)
def pre_save_create_order_id(sender, instance, *args, **kwargs):
    """
    Gera um id único e seguro antes que o objeto seja salvo.
    """
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)

# Nota: Não precisamos do pre_save.connect() aqui, pois o @receiver já faz isso.
# pre_save.connect(pre_save_create_order_id, sender = Order)