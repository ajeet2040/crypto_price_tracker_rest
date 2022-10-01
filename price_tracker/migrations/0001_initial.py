# Generated by Django 4.1.1 on 2022-10-01 11:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('coin', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=25)),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]