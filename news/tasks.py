from celery import shared_task
import datetime

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Post, Category, PostCategory


@shared_task
def weekly_mail():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(time_in__gte=last_week)
    categories = set(posts.values_list('category__postcategory', flat=True))
    subscribers = set(Category.objects.filter(postcategory__in=categories).values_list('subscribers__email', flat=True))
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )

    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def send_notifications(pk):
    post = Post.objects.get(pk=pk)
    categories = post.category.all()
    title = post.title
    subscribers = []
    for category in categories:
        subscribers_user = category.subscribers.all()
        for user in subscribers_user:
            subscribers.append(user.email)
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': post.preview,
            'link': f'{settings.SITE_URL}/{pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

