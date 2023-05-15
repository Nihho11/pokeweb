# Generated by Django 4.2.1 on 2023-05-12 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('pais', models.CharField(default='', max_length=25)),
                ('dni', models.CharField(default='00000000', max_length=8)),
                ('vigente', models.BooleanField(default=True)),
            ],
        ),
    ]
