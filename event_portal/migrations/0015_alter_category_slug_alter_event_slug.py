# Generated by Django 4.1.7 on 2023-02-27 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_portal', '0014_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(editable=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]
