# Generated by Django 2.2.12 on 2020-05-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheetbot', '0005_auto_20200510_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='working_timezone',
            field=models.CharField(default='CET', max_length=31),
        ),
    ]