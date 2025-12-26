from django.db.models.signals import pre_save, m2m_changed
from django.dispatch import receiver
from .models import Cart
from decimal import Decimal

# Usando o decorator @receiver fica ainda mais limpo!
@receiver(m2m_changed, sender=Cart.products.through)
def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        products = instance.products.all()
        total = 0
        for product in products:
            total += product.price
        
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()

@receiver(pre_save, sender=Cart)
def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        #instance.total = instance.subtotal  + 10 # considere o 10 como uma taxa de entrega
        instance.total = Decimal(instance.subtotal) * Decimal(1.08) # 8% de taxa
    else:
        instance.total = 0.00