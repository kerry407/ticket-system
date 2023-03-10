# Generated by Django 4.1.7 on 2023-03-06 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_portal', '0016_rename_tags_event_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_time',
            new_name='event_end_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_date',
        ),
        migrations.AddField(
            model_name='event',
            name='event_end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_start_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_start_time',
            field=models.TimeField(null=True),
        ),
    ]
