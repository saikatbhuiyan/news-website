# Generated by Django 2.2.5 on 2020-05-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200424_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='abouttxt',
            field=models.CharField(default='-', max_length=255),
        ),
        migrations.AlterField(
            model_name='main',
            name='about',
            field=models.TextField(default='-'),
        ),
    ]
