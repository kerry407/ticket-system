# Generated by Django 4.1.7 on 2023-02-24 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_portal', '0008_remove_event_ticket_price_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
