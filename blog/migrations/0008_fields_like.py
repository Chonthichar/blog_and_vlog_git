# Generated by Django 4.2.7 on 2023-11-05 10:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_fields_authorhidden'),
    ]

    operations = [
        migrations.AddField(
            model_name='fields',
            name='like',
            field=models.ManyToManyField(related_name='blog_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
