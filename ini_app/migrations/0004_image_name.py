# Generated by Django 3.0.5 on 2020-04-10 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ini_app', '0003_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default='img', max_length=255),
        ),
    ]
