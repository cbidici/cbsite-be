# Generated by Django 3.2.6 on 2021-08-27 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='site',
        ),
    ]
