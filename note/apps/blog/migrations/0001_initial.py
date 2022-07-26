# Generated by Django 4.0.5 on 2022-07-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, verbose_name='Автор реценции')),
                ('title', models.CharField(max_length=100, verbose_name='Тайтл')),
                ('text', models.TextField(verbose_name='Текст реценции')),
            ],
            options={
                'verbose_name': 'Рецензия',
                'verbose_name_plural': 'Рецензия',
            },
        ),
    ]
