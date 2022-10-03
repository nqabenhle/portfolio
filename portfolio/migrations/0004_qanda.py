# Generated by Django 4.1.1 on 2022-10-03 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_certificate_picture_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='QAndA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Anonymous', max_length=50)),
                ('question', models.TextField(max_length=1000)),
                ('answer', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
