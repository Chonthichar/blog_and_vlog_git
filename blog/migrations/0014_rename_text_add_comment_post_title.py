# Generated by Django 4.2.7 on 2023-11-06 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_add_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_comment',
            old_name='text',
            new_name='post_title',
        ),
    ]
