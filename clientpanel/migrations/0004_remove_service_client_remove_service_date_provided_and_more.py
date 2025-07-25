# Generated by Django 5.2.1 on 2025-06-25 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientpanel', '0003_alter_service_date_provided'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='client',
        ),
        migrations.RemoveField(
            model_name='service',
            name='date_provided',
        ),
        migrations.AlterField(
            model_name='client',
            name='services',
            field=models.ManyToManyField(blank=True, related_name='clients', to='clientpanel.service'),
        ),
    ]
