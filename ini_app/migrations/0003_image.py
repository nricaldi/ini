# Generated by Django 3.0.5 on 2020-04-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ini_app', '0002_delete_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='media')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]