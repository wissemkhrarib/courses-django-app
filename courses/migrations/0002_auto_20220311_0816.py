# Generated by Django 2.2.14 on 2022-03-11 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lesson',
            name='num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='level',
            name='num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject',
            name='num',
            field=models.IntegerField(default=0),
        ),
    ]
