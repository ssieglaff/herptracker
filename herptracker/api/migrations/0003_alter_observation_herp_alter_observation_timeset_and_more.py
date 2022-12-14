# Generated by Django 4.1.2 on 2022-12-15 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_observation_herp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='herp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.herp'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='timeSet',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='trapType',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
