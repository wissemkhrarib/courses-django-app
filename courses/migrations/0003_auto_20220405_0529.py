# Generated by Django 2.2.14 on 2022-04-05 05:29

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20220311_0816'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={'ordering': ['num']},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['num']},
        ),
        migrations.AlterModelOptions(
            name='level',
            options={'ordering': ['num']},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['num']},
        ),
        migrations.AddField(
            model_name='lesson',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
