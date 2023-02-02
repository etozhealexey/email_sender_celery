from django.core.mail import send_mail
from send_mail.celery import app

from .service import send
from .models import Contact

@app.task
def send_spam_email(user_email):
    send(user_email)

@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            "Вы подпиисались на рассылку",
            "Мы будем присылать Вам много спама каждые 10 минут.",
            "djangosc876@gmail.com",
            [user_email],
            fail_silently=False,
        )

#можно добавить переменные в ф стринг для уточнения имени, даты рождения и прочего