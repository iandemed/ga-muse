# Generated by Django 3.1.2 on 2020-10-02 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img_url',
            field=models.URLField(max_length=480),
        ),
    ]
