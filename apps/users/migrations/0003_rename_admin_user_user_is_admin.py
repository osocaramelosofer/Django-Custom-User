# Generated by Django 4.0.3 on 2022-04-11 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='admin_user',
            new_name='is_admin',
        ),
    ]
