# Generated by Django 3.2.9 on 2021-12-03 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='checked',
            field=models.BooleanField(default=False, verbose_name='Обработано'),
        ),
    ]