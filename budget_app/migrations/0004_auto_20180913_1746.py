# Generated by Django 2.1 on 2018-09-13 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0003_auto_20180906_2003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biaya',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterField(
            model_name='biaya',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=30),
        ),
    ]