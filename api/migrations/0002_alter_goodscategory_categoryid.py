# Generated by Django 3.2.15 on 2023-02-27 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodscategory',
            name='categoryID',
            field=models.IntegerField(help_text='类别ID', primary_key=True, serialize=False, unique=True),
        ),
    ]