# Generated by Django 2.1 on 2018-09-13 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polling_app', '0002_auto_20180913_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='poll',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='poll',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='user',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
