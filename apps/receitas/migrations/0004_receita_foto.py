# Generated by Django 3.1.3 on 2020-11-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0003_receita_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto',
            field=models.ImageField(blank=True, upload_to='receitas/fotos/'),
        ),
    ]
