# Generated by Django 3.2.16 on 2024-08-30 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_follow_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='user',
            field=models.SlugField(unique=True),
        ),
    ]
