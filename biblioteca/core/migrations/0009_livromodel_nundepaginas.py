# Generated by Django 4.2.6 on 2023-10-30 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_livromodel_ano'),
    ]

    operations = [
        migrations.AddField(
            model_name='livromodel',
            name='nunDePaginas',
            field=models.CharField(default=123, max_length=3, verbose_name='Número de páginas do livro'),
            preserve_default=False,
        ),
    ]
