from celery import shared_task
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Order


@shared_task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.user.first_name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'
    html_page = render_to_string('orders/order_recieved_email.html', {
        'user': order.user,
        'order': order,
    })

    msg = EmailMultiAlternatives(subject, message, 'imjuni.pythondev@gmail.com', [order.user.email])

    msg.attach_alternative(html_page, "text/html")
    return msg.send(fail_silently=False)

    # mail_sent = send_mail(subject,
    #                       message,
    #                       'imjuni.pythondev@gmail.com',
    #                       [order.user.email])
    # return mail_sent
