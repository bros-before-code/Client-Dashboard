# Generated by Django 5.2.1 on 2025-06-24 17:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientpanel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='services',
            field=models.ManyToManyField(related_name='clients', to='clientpanel.service'),
        ),
        migrations.AlterField(
            model_name='service',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_entries', to='clientpanel.client'),
        ),
    ]
