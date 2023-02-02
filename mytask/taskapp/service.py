from django.core.mail import send_mail

def send(user_email):
    send_mail(
        "Вы подпиисались на рассылку",
        "Мы будем присылать Вам много спама.",
        "djangosc876@gmail.com",
        [user_email],
        fail_silently=False,



    )