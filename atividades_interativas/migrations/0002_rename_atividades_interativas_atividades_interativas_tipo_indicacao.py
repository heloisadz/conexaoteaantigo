# Generated by Django 4.2.6 on 2024-05-22 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atividades_interativas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atividades_interativas',
            old_name='atividades_interativas',
            new_name='tipo_indicacao',
        ),
    ]
