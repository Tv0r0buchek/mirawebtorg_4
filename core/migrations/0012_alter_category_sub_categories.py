# Generated by Django 4.0.4 on 2022-06-03 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_category_sub_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='sub_categories',
            field=models.ManyToManyField(blank=True, to='core.category'),
        ),
    ]
