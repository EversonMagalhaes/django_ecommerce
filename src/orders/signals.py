from ecommerce.utils import unique_order_id_generator
from django.db.models.signals import pre_save, post_save
from .models import Order
from django.dispatch import receiver
from carts.models import Cart

@receiver(pre_save, sender=Order)
def pre_save_create_order_id(sender, instance, *args, **kwargs):
    """
    Gera um id único e seguro antes que o objeto seja salvo.
    """
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)
    # retorna todos os orders com esta instância de cart, 
    # excluindo aqueles que têm a mesma instância de billing_profile
    qs = Order.objects.filter(cart = instance.cart).exclude(billing_profile = instance.billing_profile)
    if qs.exists():
        qs.update(active=False)

# Nota: Não precisamos do pre_save.connect() aqui, pois o @receiver já faz isso.
# pre_save.connect(pre_save_create_order_id, sender = Order)

@receiver(post_save, sender=Cart)
def post_save_cart_total(sender, instance, created, *args, **kwargs):
    """
    Quando o carrinho é alterado, atualiza o total da Order associada.
    """
    if not created:
        cart_obj = instance
        cart_total = cart_obj.total
        cart_id = cart_obj.id
        qs = Order.objects.filter(cart__id=cart_id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()

@receiver(post_save, sender=Order)
def post_save_order(sender, instance, created, *args, **kwargs):
    """
    Quando a Order é criada, calcula o seu próprio total.
    """
    print("Executando")
    if created:
        print("Atualizando")
        instance.update_total()