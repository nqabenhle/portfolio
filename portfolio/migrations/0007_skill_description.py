# Generated by Django 4.1.1 on 2022-10-11 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='description',
            field=models.TextField(default='description', max_length=1000),
            preserve_default=False,
        ),
    ]
