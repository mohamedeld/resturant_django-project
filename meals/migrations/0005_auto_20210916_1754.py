# Generated by Django 3.2.7 on 2021-09-16 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0004_meals_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='meals',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
