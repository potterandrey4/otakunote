# Generated by Django 4.0.5 on 2022-07-24 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_genrefilm_rename_genre_genrebook_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serial',
            options={'ordering': ['-created_date'], 'verbose_name': 'Сериал', 'verbose_name_plural': 'Сериалы'},
        ),
        migrations.AddField(
            model_name='book',
            name='type_book',
            field=models.CharField(choices=[('Книга', 'Книга'), ('Фанфик', 'Фанфик'), ('Манга', 'Манга'), ('Манхва', 'Манхва'), ('Комикс', 'Комикс')], default='Книга', max_length=10),
        ),
        migrations.AddField(
            model_name='film',
            name='type_film',
            field=models.CharField(choices=[('Южная Корея', 'Южная Корея'), ('Япония', 'Япония'), ('Китай', 'Китай'), ('США', 'США'), ('Россия', 'Россия'), ('Другое', 'Другое')], default='Не выбрано', max_length=11),
        ),
        migrations.AddField(
            model_name='serial',
            name='type_serial',
            field=models.CharField(choices=[('Южная Корея', 'Южная Корея'), ('Япония', 'Япония'), ('Китай', 'Китай'), ('США', 'США'), ('Россия', 'Россия'), ('Другое', 'Другое')], default='Не выбрано', max_length=11),
        ),
        migrations.AlterField(
            model_name='book',
            name='lastpage',
            field=models.IntegerField(verbose_name='Cтраница'),
        ),
    ]
