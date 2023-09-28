from django.db.models.signals import post_save
from django.dispatch import receiver
from robots.models import Robot
from orders.models import Order
from django.core.mail import send_mail


@receiver(post_save, sender=Robot)
def notify_customer_robot_available(sender, instance, created, **kwargs):
    if created:
        serial = instance.serial
        model, version = serial.split("-")
        pending_orders = Order.objects.filter(
            robot_serial=serial, robot_available=False
        )
        if pending_orders.exists():
            for order in pending_orders:
                customer = order.customer
                customer_email = customer.email
                subject = "Робот доступен"
                message = f"Добрый день!\nНедавно вы интересовались нашим роботом модели {model}, версии {version}.\n"
                message += "Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами."
                from_email = "tensaelden@yandex.ru"
                recipient_list = [customer_email]
                send_mail(
                    subject, message, from_email, recipient_list, fail_silently=False
                )
                order.robot_available = True
                order.save()
