# Generated by Django 4.1.7 on 2023-04-27 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stech', '0002_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='logos/')),
            ],
        ),
    ]
