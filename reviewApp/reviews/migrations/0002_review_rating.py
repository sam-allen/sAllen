# Generated by Django 2.2 on 2019-04-23 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=0, max_length=5),
        ),
    ]