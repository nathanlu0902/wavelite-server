# Generated by Django 4.1.6 on 2023-02-02 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(blank=True, max_length=32, null=True)),
                ('phonenumber', models.CharField(blank=True, max_length=11, null=True)),
                ('level', models.CharField(blank=True, max_length=16, null=True)),
                ('account_status', models.CharField(blank=True, max_length=10, null=True)),
                ('birth', models.DateField(blank=True, null=True)),
                ('created_by', models.DateField()),
                ('gender', models.CharField(blank=True, choices=[('m', 'male'), ('f', 'female')], max_length=1, null=True)),
            ],
            options={
                'ordering': ['created_by'],
            },
        ),
    ]
