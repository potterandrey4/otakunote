# Generated by Django 4.0.5 on 2022-07-24 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_serial_options_book_type_book_film_type_film_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='country_film',
            field=models.CharField(choices=[('Другое', 'Другое'), ('Южная Корея', 'Южная Корея'), ('Япония', 'Япония'), ('Китай', 'Китай'), ('США', 'США'), ('Россия', 'Россия')], default='Не выбрано', max_length=11),
        ),
        migrations.AlterField(
            model_name='film',
            name='type_film',
            field=models.CharField(choices=[('Фильм', 'Фильм'), ('Аниме', 'Аниме'), ('Мульт', 'Мульт')], default='Не выбрано', max_length=11),
        ),
        migrations.AlterField(
            model_name='serial',
            name='type_serial',
            field=models.CharField(choices=[('Другое', 'Другое'), ('Южная Корея', 'Южная Корея'), ('Япония', 'Япония'), ('Китай', 'Китай'), ('США', 'США'), ('Россия', 'Россия')], default='Не выбрано', max_length=11),
        ),
    ]
