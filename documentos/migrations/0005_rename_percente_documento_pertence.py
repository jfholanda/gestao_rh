# Generated by Django 4.2.5 on 2023-09-14 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0004_documento_arquivo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documento',
            old_name='percente',
            new_name='pertence',
        ),
    ]
