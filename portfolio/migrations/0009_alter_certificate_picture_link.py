# Generated by Django 4.1.1 on 2022-11-11 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_skill_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='picture_link',
            field=models.CharField(max_length=500),
        ),
    ]
