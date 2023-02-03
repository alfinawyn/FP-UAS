# Generated by Django 4.1.5 on 2023-02-02 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_pakaian'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hijab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodebrg', models.CharField(max_length=8)),
                ('nama', models.CharField(max_length=50)),
                ('stok', models.IntegerField()),
                ('harga', models.BigIntegerField()),
                ('link_gbr', models.CharField(blank=True, max_length=150)),
                ('kategori', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.jenis')),
            ],
        ),
    ]
