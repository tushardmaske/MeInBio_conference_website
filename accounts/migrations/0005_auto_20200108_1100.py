# Generated by Django 2.2.9 on 2020-01-08 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200108_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='abstract',
            field=models.TextField(default='_'),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='bio',
            field=models.TextField(default='_'),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='key_words',
            field=models.CharField(default='_', max_length=500),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='title',
            field=models.CharField(default='_', max_length=500),
        ),
    ]
