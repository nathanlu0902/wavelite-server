# Generated by Django 3.2.15 on 2023-02-27 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20230227_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]