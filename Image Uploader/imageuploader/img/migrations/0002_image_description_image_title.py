# Generated by Django 4.1.5 on 2023-05-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
