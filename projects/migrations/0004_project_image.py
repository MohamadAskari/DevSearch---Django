# Generated by Django 3.2.6 on 2021-08-29 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210828_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default='static/images/default.jpg', null=True, upload_to=''),
        ),
    ]
