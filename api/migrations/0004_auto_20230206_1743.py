# Generated by Django 3.2.15 on 2023-02-06 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20230203_1746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='nickname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='phonenumber',
            new_name='phone',
        ),
    ]
