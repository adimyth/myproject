# Generated by Django 2.1.5 on 2019-01-27 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_app', '0003_auto_20190120_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
