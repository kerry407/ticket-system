# Generated by Django 4.1.7 on 2023-03-12 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_delete_hostuserprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('company_description', models.TextField(blank=True, max_length=500)),
                ('website_url', models.URLField(blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('zip_code', models.CharField(blank=True, max_length=20)),
                ('twitter', models.URLField(blank=True, max_length=100)),
                ('facebook', models.URLField(blank=True, max_length=100)),
                ('instagram', models.URLField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
