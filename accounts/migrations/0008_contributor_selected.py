# Generated by Django 2.2.9 on 2020-01-11 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200109_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='selected',
            field=models.BooleanField(default=False),
        ),
    ]
