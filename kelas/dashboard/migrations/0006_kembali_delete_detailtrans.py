# Generated by Django 4.1.3 on 2023-02-01 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_pinjam_delete_transaksi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kembali',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_buku', models.CharField(max_length=10)),
                ('nama', models.CharField(max_length=8)),
                ('tgl_pinjam', models.DateTimeField(auto_now_add=True)),
                ('tgl_kembali', models.DateTimeField(auto_now_add=True)),
                ('kondisi', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Detailtrans',
        ),
    ]
