# Generated by Django 5.2.1 on 2025-06-25 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientpanel', '0002_client_services_alter_service_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='date_provided',
            field=models.DateField(blank=True, null=True),
        ),
    ]
