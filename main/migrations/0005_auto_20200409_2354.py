# Generated by Django 2.2.5 on 2020-04-09 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200409_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='fb',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='main',
            name='tw',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='main',
            name='yt',
            field=models.TextField(),
        ),
    ]
