# Generated by Django 4.1 on 2022-08-17 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eicerik', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='title',
            new_name='baslık',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='number_of_pages',
            new_name='sayfa_sayısı',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='yazar',
        ),
    ]
