# Generated by Django 4.1.5 on 2023-02-02 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_hijab'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aksesoris',
            old_name='kodebrg',
            new_name='kodeaks',
        ),
        migrations.RenameField(
            model_name='hijab',
            old_name='kodebrg',
            new_name='kodehjb',
        ),
        migrations.RenameField(
            model_name='pakaian',
            old_name='kodebrg',
            new_name='kodepkn',
        ),
    ]
