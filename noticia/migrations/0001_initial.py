# Generated by Django 4.2.6 on 2024-05-22 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=150)),
                ('idNo', models.CharField(default='-', max_length=11, primary_key=True, serialize=False, unique=True)),
                ('idade', models.IntegerField()),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=30)),
                ('identificacao', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=200)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
    ]
