# Generated by Django 3.0.5 on 2020-04-10 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ini_app', '0004_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.FileField(upload_to=''),
        ),
    ]