# Generated by Django 3.1.2 on 2020-11-01 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('ingredients', models.CharField(max_length=250)),
                ('time', models.IntegerField()),
            ],
        ),
    ]
