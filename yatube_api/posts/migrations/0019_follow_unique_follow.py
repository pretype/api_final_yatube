# Generated by Django 3.2.16 on 2024-08-30 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_alter_follow_following'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('following', 'user'), name='unique_follow'),
        ),
    ]
