# Generated by Django 4.2.6 on 2023-10-29 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_livromodel_ano'),
    ]

    operations = [
        migrations.AddField(
            model_name='livromodel',
            name='isbn',
            field=models.CharField(default=1020304050601, max_length=13, verbose_name='ISBN do livro'),
            preserve_default=False,
        ),
    ]