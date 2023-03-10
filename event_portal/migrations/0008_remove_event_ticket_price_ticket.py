# Generated by Django 4.1.7 on 2023-02-24 21:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('event_portal', '0007_alter_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='ticket_price',
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ticket_type', models.CharField(max_length=25)),
                ('ticket_price', models.FloatField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_portal.event')),
            ],
        ),
    ]
